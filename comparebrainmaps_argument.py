import argparse
from neuromaps import datasets,nulls,stats,images,parcellate
from neuromaps.resampling import resample_images
import nibabel as nib
from neuromaps import stats
from nilearn.datasets import fetch_atlas_surf_destrieux
import yaml
import glob
import pandas as pd
import numpy as np 
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir",type=str,required=True,help="传入需要比较的脑图")
    parser.add_argument("--annotation_source",type=str,default=None,required=False,help="比较脑图的source")
    parser.add_argument("--annotation_desc",default=None,type=str,required=False,help="比较脑图的desc")
    parser.add_argument("--annotation_space",default=None,type=str,required=False,help="比较脑图的space")
    parser.add_argument("--annotation_den",default=None,type=str,required=False,help="比较脑图的density")
    parser.add_argument("--src_space",type=str,required=True,help="src脑图的空间")
    parser.add_argument("--trg_space",type=str,required=True,help="trg脑图的空间")
    parser.add_argument("--method",default='linear',type=str,required=False,help="比较脑图的方法")
    parser.add_argument("--resampling",default='downsample_only',type=str,required=False,help="重采样 src 和 trg 的重采样函数的名称。必须是以下之一：“downsample_only”、“transform_to_src”、“transform_to_trg”、“transform_to_alt”")
    parser.add_argument("--alt_spec",default=None,type=str,required=False,nargs='+',help="其中条目是所需目标空间的（空间、密度）。")
    parser.add_argument("--nulls",default="nulls.alexander_bloch",type=str,required=False)
    parser.add_argument("--atlas",default="fsaverage",type=str,required=False)
    parser.add_argument("--density",default="10k",type=str,required=False)
    parser.add_argument("--n_perm",default=100,type=int,required=False)
    parser.add_argument("--seed",default=1000,type=int,required=False)
    parser.add_argument("--map_left",default="test_gii/left.gii",type=str,required=False)
    parser.add_argument("--map_right",default="test_gii/right.gii",type=str,required=False)
    if num == '2':
        args = parser.parse_args()
        src_map = nib.load(args.data_dir)
        trg_map= datasets.fetch_annotation(source=args.annotation_source, desc=args.annotation_desc,space=args.annotation_space,den=args.annotation_den,return_single=True)
        src_mapr,trg_mapr = resample_images(src=src_map,trg=trg_map,\
            src_space=args.src_space,trg_space=args.trg_space,\
                method=args.method,resampling=args.resampling,\
            alt_spec=args.alt_spec)
        Nulls = eval(args.nulls)
        map_left = args.map_left
        map_right= args.map_right 
        parc_left = nib.load(map_left)
        parc_right = nib.load(map_right)
        parcellation = images.relabel_gifti((parc_left,parc_right))
        destrieux = parcellate.Parcellater(parcellation, args.atlas).fit()
        src_parc = destrieux.transform(src_mapr, args.atlas)
        trg_parc = destrieux.transform(trg_mapr, args.atlas)
        parcellation1 = images.relabel_gifti((parc_left,parc_right))
        rotated = Nulls(src_parc, atlas=args.atlas,density=args.density,
                                    n_perm=args.n_perm, seed=args.seed,parcellation=parcellation1)

        try:
            corr ,pval= stats.compare_images(src_parc, trg_parc,nulls=rotated)
        except:
            raise ValueError("rotated 维度不同")
        print(f'Correlation: r = {corr:.02f},p={pval:.03f}')
    else:

        args = parser.parse_args()
        src_map = nib.load(args.data_dir)
        trg_map= datasets.fetch_annotation(source=args.annotation_source, desc=args.annotation_desc,space=args.annotation_space,den=args.annotation_den,return_single=True)
        src_mapr,trg_mapr = resample_images(src=src_map,trg=trg_map,\
            src_space=args.src_space,trg_space=args.trg_space,\
                method=args.method,resampling=args.resampling,\
            alt_spec=args.alt_spec)
        Nulls = eval(args.nulls)
        # print(type(Nulls))
        rotated = Nulls(src_mapr, atlas=args.atlas,density=args.density,
                                    n_perm=args.n_perm, seed=args.seed)
        corr ,pval= stats.compare_images(src_mapr, trg_mapr,nulls=rotated)
        print(f'Correlation: r = {corr:.02f},p={pval:.03f}')

if __name__ =="__main__":
    num = input("请输入数字 1.Nulls with non-parcellated data，2、Nulls with parcellated data，3、Nulls for volumetric data")
    main()   

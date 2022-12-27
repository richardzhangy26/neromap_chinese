from neuromaps import datasets,nulls,stats,images,parcellate
from neuromaps.resampling import resample_images
import nibabel as nib
from neuromaps import stats
from nilearn.datasets import fetch_atlas_surf_destrieux
import yaml
import glob
import pandas as pd
import numpy as np 
# method to change dataframe to Csv
def OutToCsv(columns,data_list):
    data = pd.DataFrame(columns=columns,data=data_list,index=None)
    if num1 =='0':
        data = data.drop(["Pval"],axis=1)
        data.to_csv("./output.csv",encoding="gbk") 
    else:
        data.to_csv("./output.csv",encoding="gbk")
    print("output结果转入到csv")
def main(data):
    data_list = []
    if num2 == '2':
        for nii in glob.glob(rf"{data['data_dir']}/*"):
            src_map = nib.load(nii)
            trg_map= datasets.fetch_annotation(source=data['annotation_source'], desc=data['annotation_desc'],space=data['annotation_space'],den=data['annotation_den'],return_single=True)
            src_mapr,trg_mapr = resample_images(src=src_map,trg=trg_map,\
                src_space=data['src_space'],trg_space=data['trg_space'],\
                    method=data['method'],resampling=data['resampling'],\
                alt_spec=(data['alt_spec'][0],data['alt_spec'][1]))
            Nulls = eval(data['nulls'])
            map_left =data['map_left']
            map_right= data['map_right']
            map_left = nib.load(map_left)
            map_right = nib.load(map_right)
            parcellation = images.relabel_gifti((map_left,map_right),background=['Medial_wall'])
            destrieux = parcellate.Parcellater(parcellation, data['atlas']).fit()
            src_parc = destrieux.transform(src_mapr, data['atlas'])
            trg_parc = destrieux.transform(trg_mapr, data['atlas'])
            rotated = Nulls(src_parc, atlas=data['atlas'],density=data['density'],
                                        n_perm=data['n_perm'], seed=data['seed'],parcellation=parcellation)
            # rotated不知道为啥是（147，100）应该是（148，100)
            try:
                corr ,pval= stats.compare_images(src_parc, trg_parc,nulls=rotated)
            except:
                print(f"rotated维度为{rotated.shape},实际需要{src_parc.shape},所以对rotated增加或着减少维度")
                zero = np.zeros(100,dtype="float32")
                rotated = np.insert(rotated,-1,zero,axis=0)
                corr ,pval= stats.compare_images(src_parc, trg_parc,nulls=rotated) 
            data_list.append([nii.split("/")[-1],round(corr,2),round(pval,2)])
            print(f'Correlation: r = {corr:.02f},p={pval:.03f}')
    else:
        for nii in glob.glob(rf"{data['data_dir']}/*"):
            src_map = nib.load(nii)
            trg_map= datasets.fetch_annotation(source=data['annotation_source'], desc=data['annotation_desc'],space=data['annotation_space'],den=data['annotation_den'],return_single=True)
            src_mapr,trg_mapr = resample_images(src=src_map,trg=trg_map,\
                src_space=data['src_space'],trg_space=data['trg_space'],\
                    method=data['method'],resampling=data['resampling'],\
                alt_spec=(data['alt_spec'][0],data['alt_spec'][1]))
            Nulls = eval(data['nulls'])
            # print(type(Nulls))
            rotated = Nulls(src_mapr, atlas=data['atlas'],density=data['density'],
                                        n_perm=data['n_perm'], seed=data['seed'])
            corr ,pval= stats.compare_images(src_mapr, trg_mapr,nulls=rotated)
            print(f'nii:{nii.split("/")[-1]} Correlation: r = {corr:.02f},p={pval:.03f}')
            data_list.append([nii.split("/")[-1],round(corr,2),round(pval,2)])
            # print(data_list)
    return data_list
if __name__ =="__main__":
    num1 = input("选择是否计算Pvalue,0表示不计算,默认计算")
    columns_name =["脑图名","Correlation","Pval"]
    print("请输入\n1.Nulls with non-parcellated surface data or volumetric data \n2、Nulls with parcellated data\n")
    num2= input("请输入选项")
    #加载yaml配置
    with open("config.yaml") as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
    data_frame = main(data)
    # print(data_frame)
    OutToCsv(columns_name, data_frame)



[Github链接](https://github.com/richardzhangy26/neromap_chinese)

[Gitee链接](https://gitee.com/richardzhangy26/neromap_chinese)

# 目录结构

```
├── README.md
├── comparebrainmaps_argument.py
├── comparebrainmaps_yaml.py
├── config.yaml
├── demo.ipynb
├── output.csv
├── test_gii
│   ├── left.gii
│   └── right.gii
├── test_nii
│   ├── neg_mVSnm_vox80_cluster.nii
│   ├── neg_mVSnm_vox80_cluster的副本.nii
│   ├── neg_mVSnm_vox80_cluster的副本2.nii
│   ├── neg_mVSnm_vox80_cluster的副本3.nii
│   ├── neg_mVSnm_vox80_cluster的副本4.nii
│   ├── neg_nmVSm_vox80_cluster.nii
│   ├── neg_nmVSm_vox80_cluster的副本.nii
│   ├── neg_nmVSm_vox80_cluster的副本2.nii
│   ├── neg_nmVSm_vox80_cluster的副本3.nii
│   └── neg_nmVSm_vox80_cluster的副本4.nii
└── 安装指南.md

```

用户可选择[`comparebrainmaps_yaml.py`](##comparebrainmaps_yaml.py使用)或者[`comparebrainmaps_argument.py`](##comparebrainmaps_arguments.py使用)运行
# 参数介绍
## Comparebrainmaps操作参数选择

总共有data_dir,annotation_source,annotation_desc,annotation_space,

annotation_den,src_space,trg_space,method,resampling,alt_spec共十种参数可选择

### data_dir

传入需要比较的脑图文件夹

### annotation_source,annotation_desc,annotation_space,annotation_den

以下为需要用来比较的annotation的四个参数

source代表文章来源的简写，如**‘abagen’、'aghourian2017'**

desc表示描述脑图代表的是什么，如**’genepc‘、'feobv'**

space表示4中空间坐标系有

1. **MNI152 (volumetric) space,**
2. **fsLR (surface) space,**
3. **fsaverage (surface) space, and**
4. **CIVET (surface) space**

den表示密度分辨率的选择

以下内容为可供选择的所有annotation


- ('abagen', 'genepc1', 'fsaverage', '10k')
- ('aghourian2017', 'feobv', 'MNI152', '1mm')
- ('alarkurtti2015', 'raclopride', 'MNI152', '3mm')
- ('bedard2019', 'feobv', 'MNI152', '1mm')
- ('beliveau2017', 'az10419369', 'MNI152', '1mm')
- ('beliveau2017', 'cimbi36', 'MNI152', '1mm')
- ('beliveau2017', 'cumi101', 'MNI152', '1mm')
- ('beliveau2017', 'dasb', 'MNI152', '1mm')
- ('beliveau2017', 'sb207145', 'MNI152', '1mm')
- ('ding2010', 'mrb', 'MNI152', '1mm')
- ('dubois2015', 'abp688', 'MNI152', '1mm')
- ('dukart2018', 'flumazenil', 'MNI152', '3mm')
- ('dukart2018', 'fpcit', 'MNI152', '3mm')
- ('fazio2016', 'madam', 'MNI152', '3mm')
- ('finnema2016', 'ucbj', 'MNI152', '1mm')
- ('gallezot2010', 'p943', 'MNI152', '1mm')
- ('gallezot2017', 'gsk189254', 'MNI152', '1mm')
- ('hcps1200', 'megalpha', 'fsLR', '4k')
- ('hcps1200', 'megbeta', 'fsLR', '4k')
- ('hcps1200', 'megdelta', 'fsLR', '4k')
- ('hcps1200', 'meggamma1', 'fsLR', '4k')
- ('hcps1200', 'meggamma2', 'fsLR', '4k')
- ('hcps1200', 'megtheta', 'fsLR', '4k')
- ('hcps1200', 'megtimescale', 'fsLR', '4k')
- ('hcps1200', 'myelinmap', 'fsLR', '32k')
- ('hcps1200', 'thickness', 'fsLR', '32k')
- ('hesse2017', 'methylreboxetine', 'MNI152', '3mm')
- ('hill2010', 'devexp', 'fsLR', '164k')
- ('hill2010', 'evoexp', 'fsLR', '164k')
- ('hillmer2016', 'flubatine', 'MNI152', '1mm')
- ('jaworska2020', 'fallypride', 'MNI152', '1mm')
- ('kaller2017', 'sch23390', 'MNI152', '3mm')
- ('kantonen2020', 'carfentanil', 'MNI152', '3mm')
- ('laurikainen2018', 'fmpepd2', 'MNI152', '1mm')
- ('margulies2016', 'fcgradient01', 'fsLR', '32k')
- ('margulies2016', 'fcgradient02', 'fsLR', '32k')
- ('margulies2016', 'fcgradient03', 'fsLR', '32k')
- ('margulies2016', 'fcgradient04', 'fsLR', '32k')
- ('margulies2016', 'fcgradient05', 'fsLR', '32k')
- ('margulies2016', 'fcgradient06', 'fsLR', '32k')
- ('margulies2016', 'fcgradient07', 'fsLR', '32k')
- ('margulies2016', 'fcgradient08', 'fsLR', '32k')
- ('margulies2016', 'fcgradient09', 'fsLR', '32k')
- ('margulies2016', 'fcgradient10', 'fsLR', '32k')
- ('mueller2013', 'intersubjvar', 'fsLR', '164k')
- ('naganawa2020', 'lsn3172176', 'MNI152', '1mm')
- ('neurosynth', 'cogpc1', 'MNI152', '2mm')
- ('norgaard2020', 'flumazenil', 'MNI152', '1mm')
- ('normandin2015', 'omar', 'MNI152', '1mm')
- ('radnakrishnan2018', 'gsk215083', 'MNI152', '1mm')
- ('raichle', 'cbf', 'fsLR', '164k')
- ('raichle', 'cbv', 'fsLR', '164k')
- ('raichle', 'cmr02', 'fsLR', '164k')
- ('raichle', 'cmruglu', 'fsLR', '164k')
- ('reardon2018', 'scalinghcp', 'civet', '41k')
- ('reardon2018', 'scalingnih', 'civet', '41k')
- ('reardon2018', 'scalingpnc', 'civet', '41k')
- ('rosaneto', 'abp688', 'MNI152', '1mm')
- ('sandiego2015', 'flb457', 'MNI152', '1mm')
- ('sasaki2012', 'fepe2i', 'MNI152', '1mm')
- ('satterthwaite2014', 'meancbf', 'MNI152', '1mm')
- ('savli2012', 'altanserin', 'MNI152', '3mm')
- ('savli2012', 'dasb', 'MNI152', '3mm')
- ('savli2012', 'p943', 'MNI152', '3mm')
- ('savli2012', 'way100635', 'MNI152', '3mm')
- ('smart2019', 'abp688', 'MNI152', '1mm')
- ('smith2017', 'flb457', 'MNI152', '1mm')
- ('sydnor2021', 'SAaxis', 'fsLR', '32k')
- ('tuominen', 'feobv', 'MNI152', '2mm')
- ('turtonen2020', 'carfentanil', 'MNI152', '1mm')
- ('xu2020', 'FChomology', 'fsLR', '32k')
- ('xu2020', 'evoexp', 'fsLR', '32k')

## resample 图像需要的参数

### src_space,trg_space

src_space,trg_space分别代表自己传入的脑图空间，用来比较的脑图标识空间

### method

{'nearest', 'linear'}, optional) -- 重采样方法。如果数据是标签图像，请指定“nearest”。默认值:linear

## resampling

重采样 src 和 trg 的重采样函数的名称。必须是以下之一：“downsample_only”、“transform_to_src”、“transform_to_trg”、“transform_to_alt”。有关详细信息，请参阅注释。默认值：'downsample_only'

四种可用的重采样策略将控制src和/或trg在相关之前的重采样方式。选项包括
resampling='downsample_only'（重采样）。
来自src和trg的数据将被重采样为两个输入数据集的较低分辨率
resampling='transform_to_src'（重采样）。
来自trg的数据总是被重新采样，以匹配src的空间和分辨率
resampling='transform_to_trg'（重采样）。
来自src的数据总是被重新取样以匹配trg的空间和分辨率
resampling='transform_to_alt'（重采样）。

### alt_spec

其中条目是所需目标空间的（空间、分辨率）。仅在 resampling='transform_to_alt' 时使用。默认值：None

## 对Spatial Nulls显著性检验

### [`neuromaps.nulls`](https://netneurolab.github.io/neuromaps/api.html#module-neuromaps.nulls) 模块
该模块提供了对各种空模型的访问，可用于生成 "空 "脑图，保留原始脑图的空间自相关方面。(关于这些模型的回顾，请参考Markello & Misic, 2021, NeuroImage）

有四种可用的空（nulls）模型可用于体素和顶点数据（voxel- and vertex-wise data ），八种空模型（nulls）可用于分块（parcellated）数据。有关空模型的完整列表，请参阅 neuromaps.nulls API。

[`neuromaps.nulls.alexander_bloch`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.alexander_bloch.html#neuromaps.nulls.alexander_bloch)(data[, ...])

Generates null maps from data using method from [[SN1\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.vazquez_rodriguez.html#sn1)

[`neuromaps.nulls.vazquez_rodriguez`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.vazquez_rodriguez.html#neuromaps.nulls.vazquez_rodriguez)(data[, ...])

Generates null maps from data using method from [[SN1\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.vazquez_rodriguez.html#sn1)

[`neuromaps.nulls.vasa`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.vasa.html#neuromaps.nulls.vasa)(data[, atlas, density, ...])

Generates null maps for parcellated data using method from [[SN2\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.vasa.html#sn2)

[`neuromaps.nulls.hungarian`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.hungarian.html#neuromaps.nulls.hungarian)(data[, atlas, ...])

Generates null maps for parcellated data using the Hungarian method ([[SN3\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.hungarian.html#sn3))

[`neuromaps.nulls.baum`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.baum.html#neuromaps.nulls.baum)(data[, atlas, density, ...])

Generates null maps for parcellated data using method from [[SN4\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.baum.html#sn4)

[`neuromaps.nulls.cornblath`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.cornblath.html#neuromaps.nulls.cornblath)(data[, atlas, ...])

Generates null maps for parcellated data using method from [[SN5\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.cornblath.html#sn5)

[`neuromaps.nulls.burt2018`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.burt2018.html#neuromaps.nulls.burt2018)(data[, atlas, ...])

Generates null maps for data using method from [[SN6\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.burt2018.html#sn6)

[`neuromaps.nulls.burt2020`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.burt2020.html#neuromaps.nulls.burt2020)(data[, atlas, ...])

Generates null maps for data using method from [[SN7\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.burt2020.html#sn7) and [[SN8\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.burt2020.html#sn8)

[`neuromaps.nulls.moran`](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.moran.html#neuromaps.nulls.moran)(data[, atlas, ...])

Generates null maps for data using method from [[SN9\]](https://netneurolab.github.io/neuromaps/generated/neuromaps.nulls.moran.html#sn9)



其中可选择的参数有

- **data** (*(**N**,**)* *array_like*) – Input data from which to generate null maps. The data must be parcellated and array-like. If None is provided then the resampling array will be returned instead.(**这里默认为自己传的data_dir的脑图)**

- **atlas** (*{'fsLR'**,* *'fsaverage'**,* *'civet'}**,* *optional*) – Name of surface atlas on which data are defined. Default: ‘fsaverage’

- **density** ([*str*](https://docs.python.org/3.6/library/stdtypes.html#str)*,* *optional*) – Density of atlas on which data are defined. Must be compatible with specified atlas. Default: ‘10k’

- **seed** (*{int**,* *np.random.RandomState instance**,* *None}**,* *optional*) – Seed for random number generation. Default: None

- **n_perm** ([*int*](https://docs.python.org/3.6/library/functions.html#int)*,* *optional*) – Number of null maps or permutations to generate. Default: 1000

  `--nulls nulls.alexander_bloch` 可选择的空模型，不填默认为 nulls.alexander_bloch

   `--atlas`可选择的atlas表面。如果 `resampling='transform_to_alt`，那么 这里应该与重采样的 `atlas`保持一致

  `--density 10k`可选择的altas的密度分辨率，必须与选择atlas兼容

  `--n_perm 100`可选择生成Null maps 或者permutaitions的数量， 默认100

  `--seed 1000 `随机种子设置，保证实验可重复性，默认为1000

  参考[API](https://netneurolab.github.io/neuromaps/user_guide/nulls.html#nulls-for-volumetric-data)

###  Nulls with non-parcellated data（surface）

null_map的生成需要上述9种方法和5中参数，返回值为（顶点，空值）。得到的nulls传到**stats.compare_images** 得到相似度和pvalue

### Nulls for volumetric data[](https://netneurolab.github.io/neuromaps/user_guide/nulls.html#nulls-for-volumetric-data)

大多数空间空值在以表面坐标系为代表的数据中效果最好。如果你正在处理以MNI152系统表示的数据，你必须使用以下三种空模型之一。再使用之前先在命令行输入，来安装依赖库

**`pip install brinsmash`**

- **neuromaps.nulls.burt2018（）**
- **neuromaps.nulls.burt2020()**
- **neuromaps.nulls.Moran()**

而其他可用的空模型假定所提供的数据在皮质表面上表示，这些模型更灵活。然而，它们都依赖于在内存中计算和存储所提供图像的距离矩阵，因此，对于体积图像来说，计算量非常大。

### Nulls for parcellated data（surface）

可参考[官方文档](https://netneurolab.github.io/neuromaps/user_guide/nulls.html#nulls-with-parcellated-data)
或者查看`demo.ipynb`

`--map_left`和 `--map_right`参数分别代表左右脑的gii格式的lable files。

文件夹 `test_gii`	中就是官方的左右脑的lable files

然后经过函数`relabel_gifti`更新GIFTI图像，使lable id在半球上是连续的



# 使用指南

## comparebrainmaps_yaml.py使用

首先在`config.yaml`文件配置所需参数。

![](https://cdn.jsdelivr.net/gh/richardzhangy26/Pic@main/src202212291305097.png)

具体参数介绍可见上文。

运行测试：

在vscode 或者 pycharm中点击运行

或者在当前目录的终端中输入 `python3 comparebrainmaps_yaml.py`

![image-20221206173617895](https://cdn.jsdelivr.net/gh/richardzhangy26/Pic@main/srcimage-20221206173617895.png)

第一个选项是是否选择计算pvalue，默认计算

第二个是选择有分割的脑图还是未分割的脑图，默认为未分割

然后将计算后的结果自动保存到当前文件夹下的`output.csv` excel文件中

![image-20221206174327975](https://cdn.jsdelivr.net/gh/richardzhangy26/Pic@main/srcimage-20221206174327975.png)



## comparebrainmaps_arguments.py使用

这里的使用参数与上文类似，除了`data_dir`替换为单独脑图名，其他参数类似，再终端里输入以下命令得到一个结果的脑图相关系数和pvalue。不保存csv

```
python comparebrainmaps_argument.py --data_dir test_nii/neg_mVSnm_vox80_cluster.nii  --annotation_desc  genepc1  --src_space  MNI152 --trg_space fsaverage  --resampling transform_to_alt  --alt_spec fsaverage 10k --nulls nulls.alexander_bloch --nulls nulls.alexander_bloch --density 10k --n_perm 100 --seed 1000 --map_left test_gii/left.gii --map_right test_gii/rigtht.gii
```

![image-20221206174856822](https://cdn.jsdelivr.net/gh/richardzhangy26/Pic@main/srcimage-20221206174856822.png)


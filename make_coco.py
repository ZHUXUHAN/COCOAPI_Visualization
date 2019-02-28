# import _init_paths
from pycocotools.coco import COCO
import json
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
import shutil
import os
#该文件是从coco2017获得了包括狗或猫的图片子数据集
class make_coco():
    def __init__(self):
        self.annotations = []
        self.images = []
        self.categories=[]
        self.annids=[]


    def processing(self,ann_path,copy_from_dir,copy_to_dir):
        annFile=ann_path
        coco_instance=COCO(annFile)
        imgIds=[]
        imgs=[]
        categories=[]


        catIds=coco_instance.getCatIds(catNms=['dog','cat'])

        print(catIds)#获取dog类别指定的类别列表 返回【18】
        cats = coco_instance.loadCats(catIds)#获取指定类别列表中的类别对应类别的类别信息 返回[{'name': 'dog', 'id': 18, 'supercategory': 'animal'}]
        print(cats)
        nms=[cat['name'] for cat in cats]
        print('COCO categories: \n{}\n'.format(' '.join(nms)))#返回dog

        nms = set([cat['supercategory'] for cat in cats])#去除重复的元素
        print('COCO supercategories: \n{}'.format(' '.join(nms)))#返回animal

        for i,cat in enumerate(cats):
            print('id',cat['id'])
            categories.append({'supercategory': cat['supercategory'], 'id': cat['id'],
                          'name': cat['name']})
        print(categories)
        self.categories=categories



        for cat in catIds:
            imgIds.append (coco_instance.getImgIds(catIds=cat))#注意这里是为了保证每张图可能只有猫或者或者只有狗，或者两者都有
        # print(imgIds)#获取指定类别的ima对应的id的列表
        for imgId in imgIds:
            imgs.append (coco_instance.loadImgs(imgId))#下载指定id列表的所有图片对应的标注信息,但是不是annotation



        for img_s in imgs:
            for img in img_s:
                shutil.copy(os.path.join(copy_from_dir,img['file_name']),copy_to_dir)

                self.images.append(img)
                # print(self.images)
                annIds = coco_instance.getAnnIds(imgIds=img['id'])#通过imgid来寻找每个图片对应的所有实例的标注annid的列表

                for annId in annIds:
                    self.annids.append(annId)
        num=0
        for i,annid in enumerate(self.annids):

            anns = coco_instance.loadAnns(annid)

            if anns[0]['category_id']==18 or anns[0]['category_id']==17:#这个按照你指定的类别进行筛选 如果这里不加，会带有其他物体的标注，标注信息不纯，既有狗猫还可能有其他的
                num+=1
                # anns[0]['category_id']=anns[0]['category_id']-17
                # print(anns[0])
                print("processing_img",num,'-img')
                self.annotations.append(anns[0])


    def make_json(self,json_save_path):
        # print(self.annotations)
        data_coco = {'images':self.images,'categories':self.categories,'annotations': self.annotations}
        # print(data_coco)
        json.dump(data_coco, open(json_save_path, 'w'))

demo=make_coco()
demo.processing('/home/priv-lab1/Database/MSCOCO2017/original_annotations/instances_train2017.json','/home/priv-lab1/Database/MSCOCO2017/train2017','/home/priv-lab1/workspace/zxh/My_Database/My_COCO/trainimg')
demo.make_json('/home/priv-lab1/workspace/zxh/My_Database/My_COCO/dog_cat_train.json')

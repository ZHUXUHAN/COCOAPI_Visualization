from __future__ import print_function
from pycocotools.coco import COCO
import os, sys, zipfile
import urllib.request
import shutil
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

annFile='3.json'
coco=COCO(annFile)

# # display COCO categories and supercategories
# cats = coco.loadCats(coco.getCatIds())
# nms=[cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))
#
# nms = set([cat['supercategory'] for cat in cats])
# print('COCO supercategories: \n{}'.format(' '.join(nms)))

# imgIds = coco.getImgIds(imgIds = [324158])
imgIds = coco.getImgIds(imgIds=[0])
img = coco.loadImgs(imgIds[0])[0]

I = io.imread('3.jpg')


# plt.axis('off')
# plt.imshow(I)
# plt.show()

#
#
# catIds=[]
# for ann in coco.dataset['annotations']:
#     if ann['image_id']==imgIds[0]:
#         catIds.append(ann['category_id'])
#
# plt.imshow(I)
# plt.axis('off')
#
# # annIds = coco.getAnnIds(imgIds=img['id'])
# # anns = coco.loadAnns(annIds)
# # coco.showAnns(anns)
#
# # initialize COCO api for person keypoints annotations
annFile = '3.json'
coco_kps=COCO(annFile)
#
# # load and display keypoints annotations
# # 加载肢体关键点
plt.imshow(I)
plt.axis('off')
ax = plt.gca()
annIds = coco_kps.getAnnIds(imgIds=img['id'])
anns = coco_kps.loadAnns(annIds)
coco_kps.showAnns(anns)

#
plt.show()

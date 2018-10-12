from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pylab
pylab.rcParams['figure.figsize'] = (8.0, 10.0)

#
# annFile='/Users/zhuxuhan/PycharmProjects/start/person_keypoints_val2017.json'
# coco=COCO(annFile)
#
# # cats = coco.loadCats(coco.getCatIds())
# # nms=[cat['name'] for cat in cats]
# # print('COCO categories: \n{}\n'.format(' '.join(nms)))
# #
# # nms = set([cat['supercategory'] for cat in cats])
# # print('COCO supercategories: \n{}'.format(' '.join(nms)))
#
# # catIds = coco.getCatIds(catNms=['person','dog','skateboard'])#not caption
# # imgIds = coco.getImgIds(catIds=catIds )#not caption
# imgIds = coco.getImgIds(imgIds = [0])
# # // loadImgs() 返回的是只有一个元素的列表, 使用[0]来访问这个元素
# # // 列表中的这个元素又是字典类型, 关键字有: ["license", "file_name",
# # //  "coco_url", "height", "width", "date_captured", "id"]
# img = coco.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]
#
# # 加载并显示图片,可以使用两种方式: 1) 加载本地图片, 2) 在线加载远程图片
# # 1) 使用本地路径, 对应关键字 "file_name"
# I = io.imread('/Users/zhuxuhan/PycharmProjects/start/3.jpg')
#
# # 2) 使用 url, 对应关键字 "coco_url"
# # I = io.imread(img['coco_url'])
#
#
#
# plt.imshow(I)
# plt.axis('off')
# # annIds = coco.getAnnIds(imgIds=img['id'], catIds=catIds, iscrowd=None)#not caption
# annIds = coco.getAnnIds(imgIds=img['id'],  iscrowd=None)
# anns = coco.loadAnns(annIds)
# coco.showAnns(anns)
# plt.show()

# key point
annFile = '/Users/zhuxuhan/PycharmProjects/start/1.json'
coco_kps=COCO(annFile)
# catIds = coco_kps.getCatIds(catNms=['person','dog','skateboard'])
# imgIds = coco_kps.getImgIds(catIds=catIds )
imgIds = coco_kps.getImgIds(imgIds = [396200])
# // loadImgs() 返回的是只有一个元素的列表, 使用[0]来访问这个元素
# // 列表中的这个元素又是字典类型, 关键字有: ["license", "file_name",
# //  "coco_url", "height", "width", "date_captured", "id"]
img = coco_kps.loadImgs(imgIds[np.random.randint(0,len(imgIds))])[0]

# 加载并显示图片,可以使用两种方式: 1) 加载本地图片, 2) 在线加载远程图片
# 1) 使用本地路径, 对应关键字 "file_name"
I = io.imread('/Users/zhuxuhan/PycharmProjects/start/000000396200.jpg')

# 2) 使用 url, 对应关键字 "coco_url"
# I = io.imread(img['coco_url'])


plt.imshow(I)
plt.axis('off')
ax = plt.gca()
annIds = coco_kps.getAnnIds(imgIds=img['id'])
anns = coco_kps.loadAnns(annIds)
coco_kps.showAnns(anns)
plt.show()



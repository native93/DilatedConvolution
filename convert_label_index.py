import os, cv2
import numpy as np

path = 'dataset_kitti/Kitti/KITTI_SEMANTIC/train/GT/'
output_path = 'dataset_kitti/Kitti/KITTI_SEMANTIC/train/GT_new/'

palette = [[128,0,0],[128,128,0],[128,128,128],[64,0,128],[192,128,128],[128,64,128],[64,64,0],[64,64,128],[192,192,128],[0,0,192],[0,128,192]]

file_list = os.listdir(path)
img_size = cv2.imread(path + file_list[0], 1).shape

for i in file_list:
	img = cv2.imread(path + i,1)
	output_img = np.zeros((img_size[0], img_size[1]))
	for x in xrange(img_size[0]):
		for y in xrange(img_size[1]):
			label_rgb = img[x,y,::-1].tolist()
			if label_rgb not in palette:
				label = 255
			else:
				label = palette.index(img[x,y,::-1].tolist())
			output_img[x,y] = label
	cv2.imwrite(output_path + i, output_img)

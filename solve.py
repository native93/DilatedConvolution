#! /usr/bin/env python
caffe_root = '/home/nazrul/caffe-dilation/'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
print caffe.__file__

#import surgery, score
#import surgery, score

import numpy as np
import os

#import setproctitle
#setproctitle.setproctitle(os.path.basename(os.getcwd()))

#weights = '../vgg16fc.caffemodel'


weights = './pretrained/dilation7_kitti.caffemodel'
# init
caffe.set_device(0)
caffe.set_mode_gpu()
#caffe.set_mode_cpu()

solver = caffe.SGDSolver('kitti_solver.prototxt')
#solver.net.copy_from(weights)
solver.solve()
solver.net.save('net.caffemodel') 

#interp_layers = [k for k in solver.net.params.keys() if 'up' in k]
#surgery.interp(solver.net, interp_layers)


#scoring
#val = np.loadtxt('/home/nazrul/caffe-dilation/dilation/dilation/dataset_kitti/Kitti/KITTI_SEMANTIC/test.txt', dtype=str)

#for _ in range(50):
    #solver.step(100)
    #score.seg_tests(solver, False, val, layer='score')
#solver.solve()
#solver.net.copy_from(weights)
#solver.net.forward()  # train net
#solver.test_nets[0].forward()  # test net (there can be more than one)
#solver.net.backward()
#solver.solve()

# surgeries
#interp_layers = [k for k in solver.net.params.keys() if 'up' in k]
#surgery.interp(solver.net, interp_layers)

# scoring
#val = np.loadtxt('../data/pascal/VOC2010/ImageSets/Main/val.txt', dtype=str)

#for _ in range(50):
#    solver.step(8000)
#    score.seg_tests(solver, False, val, layer='score')

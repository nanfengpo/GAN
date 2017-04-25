# encoding: utf-8

"""
@author: donald
@position: donald-elementary
@file: utils.py
@time: 2017/4/25 11:16
"""

from PIL import Image
from os.path import join
import numpy as np


def save_samples(np_imgs, img_path, cur_epoch, n_img=36):
    """
    synthesize images and save it to img_path
    Args:
        np_imgs: [N, H, W, 3] [0, 1.0] float32
        img_path: str
        cur_epoch: int
        n_imgs: int
    """
    np_imgs *= 255
    np_imgs = np_imgs.astype(np.uint8)
    H = W = int(np_imgs.shape[1] ** 0.5)
    num = int(n_img ** 0.5)
    print num
    sep = 3
    syn_img = np.ones((num * H + (num - 1) * sep, num * W + (num - 1) * sep)) * 255
    syn_img = syn_img.astype(np.uint8)
    for i in xrange(num):
        for j in xrange(num):
            syn_img[i*(H+sep):(i+1)*H+i*sep, j*(W+sep):(j+1)*W+j*sep] = \
                    np_imgs[i*num + j].reshape((28, 28))

    im = Image.fromarray(syn_img)
    im.save(join(img_path, "sample_img_%d.jpg" % cur_epoch))
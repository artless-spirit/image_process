"""
仿射变换就是线性变换+平移
线性变换：(1)变换前是直线的，变换后依然是直线
(2)变换后直线的比例保持不变
"""
import cv2
import numpy as np


def identical_transform(image):
    return image


def rotate_image(image, angle):
    pass


def translate_image(image, direction):
    pass


def deviation_image(image, direction):
    pass


def scale_image(img, scale):
    scaled = scale * img
    return scaled


if __name__ == '__main__':
    image = cv2.imread('lena.png')
    scale = np.array([[0.5, 0, 0], [0, 0.5, 0], [0, 0, 1]])
    scaled_img = scale_image(image, scale)
    cv2.imwrite("scaled.png", scaled_img)

"""
1.通过成像系统拍摄，数字化之后的图像就是一个二维数组
2.图像有单通道和多通道之分，通过访问多维矩阵的方式访问图像即可
"""
import cv2

image = cv2.imread("lena.png")
h,w,c = image.shape
# for i in range(h):
#     for j in range(w):
#         for k in range(c):
#             print(image[i][j][k])

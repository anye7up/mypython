#coding:utf-8

"""
用opencv绘制蜂窝图
"""

import cv2
import numpy as np
import math

pi = math.pi
# 绘制格子
def hexgrid(gx,gy,sl=10):
    distance = sl * math.cos(pi/6)
    x = [gx,gx + sl,gx + 1.5 * sl,  gx + sl,    gx,         gx - 0.5 * sl,  gx]
    y = [gy,gy, gy + distance,gy + 2*distance, gy + 2*distance, gy + distance, gy]
    for i in range(6):
        cv2.line(img,(int(x[i]), int(y[i])),(int(x[i+1]), int(y[i+1])), (0,0,0,255),4)

# 绘制格子地图
def hexmap(w,h):
    x = 0
    y = 0
    sl = 64
    
    distance = sl * math.cos(pi/6)
    for i in range(w):
        for j in range(h):
            hexgrid(x,y,sl)
            # print(x,y)
            y += 2 * distance
        x += sl * 1.5
        if (i % 2 == 0):
            y = distance
        else:
            y = 0


#img = range(1,255)
pw = int(input('请输入画布宽度:\n'))
ph = int(input('请输入画布高度:\n'))
img = np.zeros((pw,ph,4), np.uint8)
# img = np.ones((800,800), np.uint8)
w = int(input('请输入格子宽度几格:\n'))
h = int(input('请输入格子高度几格:\n'))
hexmap(w,h)
# cv2.imshow("fff", img)
cv2.waitKey(0)
cv2.imwrite("fff.png",img)


import numpy as np
import cv2 as cv
im=cv.imread('1.jpg')
imgray=cv.cvtColor(im,cv.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(imgray,127,255,0)
im2,contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(im,contours,-1,(0,255,0),3)
cv.imwrite('output.jpg',im)

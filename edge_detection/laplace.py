import numpy as np
import cv2 as cv
img=cv.imread('1.jpg')
# converting to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# remove noise
img = cv.GaussianBlur(gray,(3,3),0)
laplacian=cv.Laplacian(img,cv.CV_64F)
cv.imwrite('lapla.jpg',laplacian)


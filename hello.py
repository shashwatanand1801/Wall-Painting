import cv2
import numpy as np


pic = cv2.imread('pic.jpeg')

img = cv2.imread('img.png')

# Convert BGR to HSV
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_yellow = np.array([115,115,115])
upper_yellow = np.array([125,125,125])



mask = cv2.inRange(img, lower_yellow, upper_yellow)

mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)


cv2.imshow("Mask", mask)

kernel = np.ones((7, 7), np.uint8)

img_erosion = cv2.erode(mask, kernel, iterations=1)


# cv2.imshow("img_erosion", img_erosion)

img_dilation = cv2.dilate(mask, kernel, iterations=1)


# cv2.imshow("img_dilation", img_dilation)


img_erosion_dilation = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow("Dilate -> Erosion", img_erosion_dilation)


# res = cv2.bitwise_and(pic,pic,mask = img_erosion_dilation)

res = cv2.bitwise_or(pic,img_erosion_dilation)


andPic = cv2.bitwise_and(pic, img_erosion_dilation, mask=None)


print(andPic.shape)

hsv_andPic = cv2.cvtColor(andPic, cv2.COLOR_BGR2HSV)

print(andPic.shape)

# hsv_andPic[:,:,(hsv_andPic[:,:,2]>0)] = 200

h,s,v = cv2.split(hsv_andPic)


print(h.shape)


h_new = np.mod(h+100, 360).astype(np.uint8)


hsv_new = cv2.merge([h_new, s, v])

cv2.imshow("Org", pic)
cv2.imshow("Res", res)
cv2.imshow("andPic", andPic)

cv2.imshow("HSV", hsv_new)

# print(img_erosion_dilation.shape)
# print(pic.shape)

zero = np.zeros(hsv_andPic.shape).astype(np.uint8)

print(zero.shape)
print(img_erosion_dilation.shape)

mask_new = cv2.bitwise_not(img_erosion_dilation)

cv2.imshow("Mask New", mask_new)


final = cv2.bitwise_and(pic, mask_new, mask = None)

cv2.imshow("Final", final)


cv2.waitKey(0)
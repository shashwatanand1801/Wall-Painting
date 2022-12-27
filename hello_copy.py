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


cv2.imshow("img_erosion", img_erosion)

img_dilation = cv2.dilate(mask, kernel, iterations=1)


cv2.imshow("img_dilation", img_dilation)


img_erosion_dilation = cv2.erode(img_dilation, kernel, iterations=1)

cv2.imshow("Dilate -> Erosion", img_erosion_dilation)


# res = cv2.bitwise_and(pic,pic,mask = img_erosion_dilation)

res = cv2.bitwise_or(pic,img_erosion_dilation)


cv2.imshow("Org", pic)
cv2.imshow("Res", res)

_, mask = cv2.threshold(res, thresh=180, maxval=255, type=cv2.THRESH_BINARY)
# copy where we'll assign the new values
green_wall = np.copy(org)
# boolean indexing and assignment based on mask
green_wall[(mask==255).all(-1)] = [0,255,0]

fig, ax = plt.subplots(1,2,figsize=(12,6))
ax[0].imshow(cv2.cvtColor(face, cv2.COLOR_BGR2HSV))
ax[1].imshow(cv2.cvtColor(green_hair, cv2.COLOR_BGR2HSV))

# print(img_erosion_dilation.shape)
# print(pic.shape)

cv2.waitKey(0)
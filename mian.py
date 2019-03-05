import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('scans/2019_03_04/zamalowane_0004.jpg', 0)

#img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret,thresh5 = cv2.threshold(img ,230,255    , cv2.THRESH_TOZERO)
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']





edges = cv2.Canny(thresh5, 200, 210, apertureSize = 3)
plt.imshow(edges)
plt.show()

lines = cv2.HoughLines(edges, 1, np.pi/180, 200)

plt.show()
for r, theta in lines[0]:

    a = np.cos(theta)

    b = np.sin(theta)

    x0 = a * r

    y0 = b * r

    x1 = int(x0 + 1000 * (-b))

    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))

    y2 = int(y0 - 1000 * (a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)



plt.imshow(img,),plt.show()
import cv2 as cv
import os
from datetime import datetime

path = os.path.join(os.path.expanduser("~"), "Desktop")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

file = os.path.join(path, f"{get_timestamp()}.png")

img = cv.imread(f'{path}\orig.png')

if img is None:
    print("이미지 로드 실패")
    exit()

color = cv.bilateralFilter(img, 3, 120, 120)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 3)

edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,13,3)

cartoon = cv.bitwise_and(color, color, mask=edges)

cv.imwrite(file, cartoon)

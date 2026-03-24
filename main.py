import cv2 as cv
import os
from datetime import datetime

path = os.path.join(os.path.expanduser("~"), "Desktop")

def get_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

file = os.path.join(path, f"{get_timestamp()}.png")

img = cv.imread(f'{path}/orig.png')

text_queue = []

if img is None:
    print("이미지 로드 실패")
    exit()

# 색상 단순화(이미지변수, 필터링 픽셀 범위, 색상공간 임계값, 좌표공간 임계값)
# 색상공간 임계값이 클수록 비슷한 색상들이 하나의 색상으로 넓게 뭉개짐
# 좌표공간 임계값이 클수록 더 멀리있는 픽셀들까지 고려해서 뭉개짐
color = cv.bilateralFilter(img, 3, 120, 120)

# 이미지 흑백변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 블러를 통한 노이즈제거 (이미지변수, 블러처리를 할 커널 크기 (3 = 3x3))
gray = cv.medianBlur(gray, 3)
# edge따기 (이미지변수, 부여할 픽셀값, 임계값 계산, 색상, 평균 계산할 영역, 평균값에서 제외할 보정상수)
edges = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,13,3)
# 컬러 위에 스케치 덮어씌우기 (합성할 소스1, 합성할소스2, 흑백 스케치선 = mask로 사용)
cartoon = cv.bitwise_and(color, color, mask=edges)

# display해서 보여줄 사진들을 합치는 기능임
combine_imgs = cv.hconcat([img, cartoon])

h, w = img.shape[:2]

cv.putText(combine_imgs, "Original", (10,h-10), cv.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
cv.putText(combine_imgs, "Cartoon", (w+10,h-10), cv.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)

while True:
    new_queue = []
    current_time = datetime.now()  
    display_img = combine_imgs.copy()
    
    for text , start in text_queue:
        elapsed = (current_time - start).total_seconds()
        if elapsed < 1:
            cv.putText(display_img, text, (10,30), cv.FONT_HERSHEY_DUPLEX, 1, (0,0,255), 2)
            new_queue.append((text,start))
    text_queue = new_queue
    
    cv.imshow("Rendered Img", display_img)
    key = cv.waitKey(10)

    if key == ord('S') or key == ord('s'):
        cv.imwrite(file, cartoon)
        text_queue.append((f"{get_timestamp()}.png saved", datetime.now()))
        
    elif key == 27:
        break

cv.destroyAllWindows()

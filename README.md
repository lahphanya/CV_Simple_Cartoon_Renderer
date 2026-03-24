# CV_Simple_Cartoon_Renderer

OpenCV를 이용한 간단한 이미지 Cartoon Recorder입니다.

파일을 바탕화면에 'orig.png' 형태로 저장해야 인식하기 때문에 꼭 해당 파일명으로 저장 후 사용하시길 바랍니다.

파일 저장은 기본적으로 'S'를 누르면 밑에 주요 기능에 적힌 내용대로 저장이 되며 ESC로 출력 화면 종료가 가능합니다.

---

## 주요 기능

* **실시간 이미지 비교 출력 (`display_img`)**
  * 원본 이미지와 카툰 효과가 적용된 이미지를 hconcat 기능을 통해 한 화면에 출력하게 만들었습니다.
  <br>
  <img src="https://github.com/user-attachments/assets/c9bf9f6e-1c46-4360-9f5c-be50ee2f633b" width="500">

* **실시간 알림 및 간편한 저장**
  * 키보드 `S`를 누르면 화면 좌측 상단에 1초간 저장 완료 알림이 표시됩니다.
  * 캡처 화면 전체가 아닌, 카툰 효과가 렌더링 된 (`cartoon`)만 단독으로 저장됩니다.
  <br>
  <img src="https://github.com/user-attachments/assets/5b42c698-ac82-4eb2-83d6-8f91ab5ec2a6" width="500">

* **자동 파일명 지정 및 경로 저장**
  * 바탕화면(Desktop) 경로에 자동으로 파일이 저장됩니다.
  * 타임스탬프를 활용하여 덮어쓰기 방지 및 고유한 파일명을 생성합니다. (형식: `YYYYMMDD_HHMMSS.png`)

* **프로그램 종료**
  * 키보드 `ESC` 키를 누르면 프로그램이 종료됩니다.

---

## 변환 이미지 예시

  | Original | Cartoon Rendered |
  | :---: | :---: |
  | <img src="https://github.com/user-attachments/assets/3dd02ebe-1b53-4ee7-b800-0524913454b7" width="400"> | <img src="https://github.com/user-attachments/assets/41dafbe0-2125-4670-b673-83ed004a41f5" width="400"> |
  | <img src="https://github.com/user-attachments/assets/e8dac5b5-da0f-471e-99d0-a92e9b132371" width="400"> | <img src="https://github.com/user-attachments/assets/c79d60b9-00a5-48c7-8a39-6b92b5c3f9f7" width="400"> |

---

## 알고리즘의 한계성

1. 노이즈 과다추출
  * 해당 두번째 변환 이미지 화면에서 확인할수 있듯이 adaptivethreshold 특성상 텍스처나 잔주름 같은 노이즈마저 edge로 취급하기 때문에 복잡한 배경과 질감에서 노이즈가 과다 추출되는 현상이 존재합니다.

2. 세밀한 디테일 손상
  * 세세한 선명도가 유지되어야 하는 부분(2번째 사진 케릭터의 눈)까지 Bilateral filter와 Blur가 일괄적으로 강하게 적용되어 본래의 형태가 뭉개지는 현상이 존재합니다.

따라서 해당 문제점이 발생시 수동적으로 Filter 와 Threshold 의 Pixel범위를 수정하여 사용할 필요성이 존재합니다.

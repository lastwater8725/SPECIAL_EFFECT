# 이미지에 특수효과 추가하기 프로그램

## Project
- 이미지에 특수효과를 추가하는 프로그램
- 기존에 존재하는 특수효과와 딥러닝 진행시 대표적으로 추가하는 증강을 확인할 수 있는 프로그램. 

## Data
- 제작시 사용한 이미지는 제작자의 github에 존재합니다.(clone시 같이 다운도 받아집니다.)

## Folder
```
├── project.toml
├── apple.jpg
├── src/
│   ├── main.py
└── README.md
```

## Environment
- Poetry를 사용하여 가상환경을 관리하고 필요한 패키지를 설치합니다

## Code 
0. Poetry가 설치되어있지 않은 경우 다음 명령어로 poetry 설치
```
Linux, macOS - curl -sSL https://install.python-poetry.org | python3 -
Windows - (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
⬇️ e.g.
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
1. 가상환경이 없는 경우 다음 명령어로 가상환경 생성
```
poetry new <가상환경 이름>
```
2. 가상환경 활성화 및 필요한 라이브러리 설치
```
poetry shell 
poetry install
```
(다음과 비슷한 오류가 발생한다면 필요한 라이브러리 직접 설치)
```
ERROR: Ignored the following versions that require a different python version: 0.28.0 Requires-Python >=3.7, <3.11; 1.21.2 Requires-Python >=3.7,<3.11; 1.21.3 Requires-Python >=3.7,<3.11; 1.21.4 Requires-Python >=3.7,<3.11; 1.21.5 Requires-Python >=3.7,<3.11; 1.21.6 Requires-Python >=3.7,<3.11
```
라이브러리 설치 명령어
```
poetry add <라이브러리 이름>
```
⬇️ e.g.
```
AttributeError: module 'cv2' has no attribute 'xphoto'
--> poetry add opencv-contrib-python
```

3. 코드 실행 
```
python src/main.py
```

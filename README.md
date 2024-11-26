## Project
- 이미지에 특수효과를 추가하는 프로그램
- 기존에 존재하는 특수효과와 딥러닝 진행시 대표적으로 추가하는 증강을 확인할 수 있는 프로그램. 
- ! exe파일로 생성해서 할 경우 이미지 경로를 영어 혹은 exe파일과 같은 경로로 맞춰주세요.
- 모든 실행은 루트 디렉토리를 가정합니다.
- exe파일이 존재하는 구글드라이브 링크입니다
- https://drive.google.com/drive/folders/1nVYU-KJEgprNjAXGJNmNH0UO0ZdFQOgF?usp=drive_link
## Data
- 제작시 사용한 이미지는 제작자의 github에 존재합니다.(clone시 같이 다운도 받아집니다.)

## Folder 구조
```
├── project.toml
├── apple.jpg
├── src/
│   ├── main.py
└── README.md
```

## Environment
- 본 프로젝트는 window에서 진행되었습니다. window에서 진행해주세요.
- poetry 가상환경에서 진행하였습니다.
## Code 
0. poetry가 설치되어있지 않은 경우 다음 명령어로 poetry를 설치해주세요
```
Linux, macOS - curl -sSL https://install.python-poetry.org | python3 -
Windows - (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
⬇️ e.g.
```
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
(정상적인 설치가 되었지만, 다음과 같은 오류가 발생한다면 Poetry 설치 경로가 PATH 환경 변수에 추가되지 않았기 때문입니다. 환경변수를 수정해주세요)
```
poetry : 'poetry' 용어가 cmdlet, 함수, 스크립트 파일 또는 실행할 수 있는 프로그램 이름으로 인식되지 않습니다. 이름이 정
확한지 확인하고 경로가 포함된 경우 경로가 올바른지 검증한 다음 다시 시도하십시오.
위치 줄:1 문자:1
+ poetry add requests
+ ~~~~~~
    + CategoryInfo          : ObjectNotFound: (poetry:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException```
```
```
다음 단계에 따라 환경 변수를 추가합니다:
- 제어판 → 시스템 → 고급 시스템 설정으로 이동합니다.
- 환경 변수 버튼을 클릭합니다.
- 사용자 변수 중 Path를 찾아 편집 버튼을 클릭합니다.
- 경로를 새 줄에 추가하고 확인을 클릭해 저장합니다.
<사용자 기본 경로>\AppData\Roaming\Python\Scripts
```

1. 가상환경이 없는 경우 다음 명령어로 가상환경을 생성해주세요

```
poetry new <가상환경 이름>
```
⬇️ e.g.
```
poetry new special_effect
```

2. 가상환경 활성화 및 필요한 라이브러리를 설치해주세요
```
poetry shell 
poetry install
```
(다음과 비슷한 오류가 발생한다면 필요한 라이브러리 직접 설치)
```
AttributeError: module 'cv2' has no attribute 'xphoto'
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

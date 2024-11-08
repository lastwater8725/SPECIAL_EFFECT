import cv2 as cv
import numpy as np
from PyQt6.QtWidgets import *
import sys

import cv2 as cv
import numpy as np
from PyQt6.QtWidgets import *
import sys

class SpecialEffect(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('사진 특수 효과 제작')
        self.setGeometry(200, 200, 800, 200)

        # 버튼 및 레이아웃 설정
        self.pictureButton = QPushButton('사진 읽기', self)
        self.embossButton = QPushButton('엠보싱', self)
        self.cartoonButton = QPushButton('카툰', self)
        self.sketchButton = QPushButton('연필 스케치', self)
        self.oilButton = QPushButton('유화', self)
        self.warpAffineButton = QPushButton('회전', self)
        self.flippedButton = QPushButton('좌우 반전', self)
        self.brightenedButton = QPushButton('밝기', self)
        self.gaussian_noiseButton = QPushButton('가우시안 노이즈', self)
        self.cvtcolorButton = QPushButton('색상 변환', self)
        self.saveButton = QPushButton('저장', self)
        self.pickCombo = QComboBox(self)
        self.pickCombo.addItems(['엠보싱', '카툰', '연필 스케치(명암)', '연필 스케치(컬러)', '유화', '회전', '좌우 반전', '밝기', '가우시안 노이즈', '색상 변환'])
        quitButton = QPushButton('나가기', self)
        self.label = QLabel('환영합니다.', self)
        self.enter = QLabel('사진 특수효과 제작 프로그램입니다. 사진을 먼저 불러와주세요', self)
        self.enter.setStyleSheet("color: red;")

        # 버튼 위치 설정
        self.pictureButton.setGeometry(10, 10, 100, 30)
        self.embossButton.setGeometry(110, 10, 100, 30)
        self.cartoonButton.setGeometry(210, 10, 100, 30)
        self.sketchButton.setGeometry(310, 10, 100, 30)
        self.oilButton.setGeometry(410, 10, 100, 30)
        self.warpAffineButton.setGeometry(10, 40, 100, 30)
        self.flippedButton.setGeometry(110, 40, 100, 30)
        self.brightenedButton.setGeometry(210, 40, 100, 30 )
        self.gaussian_noiseButton.setGeometry(310,40,100,30)
        self.cvtcolorButton.setGeometry(410, 40, 100, 30)
        self.saveButton.setGeometry(510, 10, 100, 30)
        self.pickCombo.setGeometry(510, 40, 110, 30)
        quitButton.setGeometry(620, 10, 100, 30)
        self.label.setGeometry(10, 75, 550, 170)
        self.enter.setGeometry(10, 90, 600, 170)

        # 버튼 비활성화
        self.embossButton.setEnabled(False)
        self.cartoonButton.setEnabled(False)
        self.sketchButton.setEnabled(False)
        self.oilButton.setEnabled(False)
        self.warpAffineButton.setEnabled(False)
        self.flippedButton.setEnabled(False)
        self.brightenedButton.setEnabled(False)
        self.gaussian_noiseButton.setEnabled(False)
        self.saveButton.setEnabled(False)
        self.cvtcolorButton.setEnabled(False)

        # 버튼 클릭 이벤트
        self.pictureButton.clicked.connect(self.pictureOpenFunction)
        self.embossButton.clicked.connect(self.embossFunction)
        self.cartoonButton.clicked.connect(self.cartoonFunction)
        self.sketchButton.clicked.connect(self.sketchFunction)
        self.oilButton.clicked.connect(self.oilFunction)
        self.warpAffineButton.clicked.connect(self.warpAffinFunction)
        self.flippedButton.clicked.connect(self.flippedFunction)
        self.brightenedButton.clicked.connect(self.brightnedFunction)
        self.gaussian_noiseButton.clicked.connect(self.gaussian_noiseFunction)
        self.saveButton.clicked.connect(self.saveFunction)
        self.cvtcolorButton.clicked.connect(self.cvtcolorFunction)
        quitButton.clicked.connect(self.quitFunction)

    def pictureOpenFunction(self):
        self.label.setText('이미지를 선택해주세요.')
        fname = QFileDialog.getOpenFileName(self, '사진 읽기', './')
        
        if fname[0]:
            self.img = cv.imread(fname[0])

            if self.img is None: 
                QMessageBox.warning(self, '파일을 읽을 수 없습니다')

            # 버튼 활성화
            self.embossButton.setEnabled(True)
            self.cartoonButton.setEnabled(True)
            self.sketchButton.setEnabled(True)
            self.oilButton.setEnabled(True)
            self.warpAffineButton.setEnabled(True)
            self.saveButton.setEnabled(True)
            self.flippedButton.setEnabled(True)
            self.brightenedButton.setEnabled(True)
            self.gaussian_noiseButton.setEnabled(True)
            self.cvtcolorButton.setEnabled(True)
            cv.imshow('Painting', self.img)
        else:
            QMessageBox.warning(self, '파일을 선택해주세요')

    
    def embossFunction(self):
        femboss=np.array([[-1.0, 0.0, 0.0],[0.0, 0.0, 0.0], [0.0, 0.0, 1.0]])

        gray=cv.cvtColor(self.img,cv.COLOR_BGR2GRAY)
        gray16=np.int16(gray)
        self.emboss=np.uint8(np.clip(cv.filter2D(gray16,-1,femboss)+128,0,255))

        cv.imshow('Emboss', self.emboss)

    def cartoonFunction(self):
        self.cartoon=cv.stylization(self.img,sigma_s=60, sigma_r=0.45)
        cv.imshow('Cartoon', self.cartoon)

    def sketchFunction(self):
        self.sketch_gray, self.sketch_color=cv.pencilSketch(self.img, sigma_s=60, sigma_r=0.07, shade_factor=0.02)
        cv.imshow('Pencil sketch(gray)', self.sketch_gray)
        cv.imshow('Pencil sketch(color)', self.sketch_color)

    def oilFunction(self):
        self.oil=cv.xphoto.oilPainting(self.img,10,1,cv.COLOR_BGR2Lab)
        cv.imshow('oil painting', self.oil)

    def warpAffinFunction(self):
        rows, cols, _ = self.img.shape
        M = cv.getRotationMatrix2D((cols / 2, rows/ 2), 90, 1)
        self.rotate_image = cv.warpAffine(self.img, M, (cols, rows))
        
        cv.imshow("Rotated Image", self.rotate_image)

    def flippedFunction(self):
        self.flipped_image = cv.flip(self.img, 1)

        cv.imshow("flipped Image", self.flipped_image)

    def brightnedFunction(self):
        self.brightned_image = np.clip(self.img.astype(np.int16) +  50, 0, 255).astype(np.uint8)

        cv.imshow("Brightened Image", self.brightned_image)

    def gaussian_noiseFunction(self, mean=0, std=50):
        height, width, _ = self.img.shape  
        self.noise_image = np.copy(self.img)  
        
        noise = np.random.normal(mean, std, (height, width, 3))  
        self.noise_image = np.clip(self.noise_image + noise, 0, 255).astype(np.uint8)  

        cv.imshow('Gaussian Noise', self.noise_image)

    def cvtcolorFunction(self):
        self.cvt_image = cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

        cv.imshow("Grayscale Image", self.cvt_image)
        
    def saveFunction(self):
        fname, _ = QFileDialog.getSaveFileName(self, '파일 저장', './', 'Image Files (*.png *.jpg *.bmp)')
        
        if fname:
            if not any(fname.endswith(ext) for ext in ['.png', '.jpg', '.bmp']):
                fname += '.png'

            i = self.pickCombo.currentIndex()
            
            if i == 0 and hasattr(self, 'emboss') and self.emboss is not None:
                cv.imwrite(fname, self.emboss)
            elif i == 1 and hasattr(self, 'cartoon') and self.cartoon is not None:
                cv.imwrite(fname, self.cartoon)
            elif i == 2 and hasattr(self, 'sketch_gray') and self.sketch_gray is not None:
                cv.imwrite(fname, self.sketch_gray)
            elif i == 3 and hasattr(self, 'sketch_color') and self.sketch_color is not None:
                cv.imwrite(fname, self.sketch_color)
            elif i == 4 and hasattr(self, 'oil') and self.oil is not None:
                cv.imwrite(fname, self.oil)
            elif i == 5 and hasattr(self, 'rotate_image') and self.rotate_image is not None:
                cv.imwrite(fname, self.rotate_image)
            elif i == 6 and hasattr(self, 'flip_image') and self.flipped_image is not None:
                cv.imwrite(fname, self.flipped_image)
            elif i == 7 and hasattr(self, 'brightned_image') and self.brightned_image is not None:
                cv.imwrite(fname, self.brightned_image)
            elif i == 8 and hasattr(self, 'noise_image') and self.noise_image is not None:
                cv.imwrite(fname, self.noise_image)
            elif i == 8 and hasattr(self, 'cvt_image') and self.cvt_image is not None:
                cv.imwrite(fname, self.cvt_image)    
            else:
                QMessageBox.warning(self, "오류", "저장할 이미지가 생성되지않았습니다.")
        else:
            QMessageBox.warning(self, "오류", "저장할 파일 경로를 선택하지 않았습니다.")


    def quitFunction(self):
        cv.destroyAllWindows()
        self.close()

app = QApplication(sys.argv)
win = SpecialEffect()
win.show()
app.exec()

    
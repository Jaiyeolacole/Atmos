"""
this file creates a splash screen for the weather
"""

import sys
import time
import mainWindow 
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class splahScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SplashScreen")

        self.screen = QDesktopWidget().screenGeometry()
        self.screenWidth, self.screenHeight = (self.screen.width()), (self.screen.height())

        self.setFixedSize(900,600)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.counter = 0
        self.n = 300 #total instance

        self.timer = QTimer()
        self.timer.timeout.connect(self.loading)
        self.timer.start(100)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        layout.addWidget(self.frame)

        self.labelTitle = QLabel(self.frame)
        self.labelTitle.setObjectName('LabelTitle')
        self.labelTitle.resize(self.width() - 10, 150)
        self.labelTitle.move(0,40)
        self.labelTitle.setText("AT-Mos")
        self.labelTitle.setAlignment(Qt.AlignCenter)

        self.labelDescription = QLabel(self.frame)
        self.labelDescription.resize(self.width() - 10, 50)
        self.labelDescription.move(0, self.labelTitle.height())
        self.labelDescription.setObjectName('labelDescription')
        self.labelDescription.setText('Loading...')
        self.labelDescription.setAlignment(Qt.AlignCenter)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.resize(self.width() - 200 -10, 50)
        self.progressBar.move(100, self.labelDescription.y() + 130)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.progressBar.setFormat('%p%')
        self.progressBar.setTextVisible(True)
        self.progressBar.setRange(0, self.n)
        self.progressBar.setValue(20)

        self.labelloading = QLabel(self.frame)
        self.labelloading.resize(self.width() -10, 50)
        self.labelloading.move(0, self.progressBar.y()+ 70)
        self.labelloading.setObjectName('LabelLoading')
        self.labelloading.setAlignment(Qt.AlignCenter)
        self.labelloading.setText('Loading...')

    def loading(self):
        self.progressBar.setValue(self.counter)

        if self.counter == int(self.n * 0.3):
            self.labelDescription.setText('Fetching API...')
        elif self.counter == int(self.n * 0.8):
             self.labelDescription.setText('Starting...')
        elif self.counter >= self.n:
            self.timer.stop()
            self.close()

            time.sleep(1)

            self.myApp = mainWindow.mainUI()
            self.myApp.show()
        self.counter += 1
             



if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet("""
        #LabelTitle {
                font-size: 60px;
                color: rgb(187, 222, 237);         
             }
                      
        #labelDescription{
                font-size: 30px;
                color: rgb(194, 206, 209);
             }
        
        #LabelLoading {
                font-size: 30px;
                color: rgb(232, 232, 232);
        }

        QFrame {
                background-color: rgb(47, 68, 84);
             }

        
        QProgressBar {
                background-color: rgb(169, 120, 147);
                color: rgb(200, 200, 200);
                border-radius: 15px;
                border-style: none;
                text-align: center;
                font-size: 30px;
        } 
        QProgressBar::chunk {
                      border-radius: 15px;
                      background-color: qlineargradient(spread:pad x1: 0, x2:1, y1:0.511364, y2:0.523, stop: 0 rgb(28, 51, 52), stop: 1 rgb(55, 110, 111));
        }

   """)
    splashscreen = splahScreen()
    splashscreen.show()
    app.exec_()
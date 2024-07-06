import sys
import requests
import json

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class mainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.screen = QDesktopWidget().screenGeometry()
        self.setWindowTitle("AT-MOS weather App")
        self.screenHeight, self.screenWidth = self.screen.height(), self.screen.width()
        self.setGeometry(0, 0, self.screenWidth - 150, self.screenHeight - 150)  
        self.setStyleSheet("background-color: qlineargradient(spread:pad x1: 0, x2:1, y1:0.511364, y2:0.523, stop: 0 rgb(28, 51, 52), stop: 1 rgb(55, 110, 111));")
        icon_path = QIcon("C:/Users/zyothron/Desktop/EcoWatch/pictures/icons8-cloud-50.png")
        self.setWindowIcon(icon_path)

        self.Atmos()
        # self.get_weather()

    def Atmos(self):
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.frame = QFrame()
        self.frame.setStyleSheet("background-color: rgba(10, 15, 16, 0.8); padding: 4px; margin: 2px;")
        layout.addWidget(self.frame)

        frame_layout = QVBoxLayout()
        self.frame.setLayout(frame_layout)

        self.name = QLabel()
        self.name.setText("<strong> AT-MOS </strong>")
        self.name.setStyleSheet("background-color: red; font-size: 20px; color: white; border-radius: 10px; ")
        self.name.setObjectName("atmos")
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        frame_layout.addWidget(self.name)

        image_path = "C:/Users/zyothron/Desktop/EcoWatch/pictures/icons8-cloud-100.png"

        self.image = QLabel()
        self.image.setPixmap(QPixmap(image_path))
        self.image.setObjectName('image')
        self.image.setAlignment(Qt.AlignCenter)
        self.image.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        frame_layout.addWidget(self.image)

        self.cityLabel = QLabel("City Name: ")
        self.cityLabel.setStyleSheet("color: white; font-size: 20px;")
        self.cityLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        frame_layout.addWidget(self.cityLabel)

        self.search = QLineEdit()
        self.search.setPlaceholderText('Enter city  e.g Lagos')
        self.search.setStyleSheet("padding: 10px; border: 2px solid red; border-radius: 2px; background-color: white; font-size: 15px;")
        self.search.setObjectName('searchBar')
        self.search.setAlignment(Qt.AlignCenter)
        self.search.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        frame_layout.addWidget(self.search)

        self.button = QPushButton()
        self.button.setText("Submit")
        self.button.setToolTip("Search City")
        self.button.setObjectName("button")
        self.button.setStyleSheet(" QPushButton {text-align: center; background-color: rgb(192,172,192); font-size: 30px; border: 2px solid red; border-radius: 10px; color: black;  padding: 2px; } ")
        self.button.clicked.connect(self.get_weather)

        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        frame_layout.addWidget(self.button)

        self.weatherLabel = QLabel("Weather Information")
        self.weatherLabel.setAlignment(Qt.AlignCenter)
        self.weatherLabel.setObjectName("weatherlabel")
        self.weatherLabel.setStyleSheet("color: white; font-size: 20px; border-radius: 5px; ")
        self.weatherLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        frame_layout.addWidget(self.weatherLabel)

        self.weatherValue = QFormLayout()
        self.weatherValue.setSpacing(10)  
        frame_layout.addLayout(self.weatherValue)

        self.temp = QLabel()
        self.temp.setText("Temperature: ")
        self.temp.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.temp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.tempReturn = QLabel()
        self.tempReturn.setText("###")
        self.tempReturn.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.tempReturn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.weatherValue.addRow(self.temp, self.tempReturn)

        self.minTemp = QLabel()
        self.minTemp.setText("Minimum Temperature: ")
        self.minTemp.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.minTemp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        self.minTempReturn = QLabel()
        self.minTempReturn.setText("###")
        self.minTempReturn.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.minTempReturn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.weatherValue.addRow(self.minTemp, self.minTempReturn)

        self.maxtemp = QLabel()
        self.maxtemp.setText("Maximum Temperature: ")
        self.maxtemp.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.maxtemp.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        self.maxtempReturn = QLabel()
        self.maxtempReturn.setText("###")
        self.maxtempReturn.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.maxtempReturn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed) 
        self.weatherValue.addRow(self.maxtemp, self.maxtempReturn)

        self.pressure = QLabel()
        self.pressure.setText("Pressure: ")
        self.pressure.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.pressure.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.pressureReturn = QLabel()
        self.pressureReturn.setText("###")
        self.pressureReturn.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.pressureReturn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.weatherValue.addRow(self.pressure, self.pressureReturn)

        self.Lat = QLabel()
        self.Lat.setText("Latitude: ")
        self.Lat.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.Lat.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.LatReturn = QLabel()
        self.LatReturn.setText("###")
        self.LatReturn.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.LatReturn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.weatherValue.addRow(self.Lat, self.LatReturn)

        self.Long = QLabel()
        self.Long.setText("Longitude: ")
        self.Long.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.Long.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.LongReturn = QLabel()
        self.LongReturn.setText("###")
        self.LongReturn.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.LongReturn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.weatherValue.addRow(self.Long, self.LongReturn)

        self.description = QLabel()
        self.description.setText("Description: ")
        self.description.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.descriptionReturn = QLabel()
        self.descriptionReturn.setText("###")
        self.descriptionReturn.setStyleSheet("color: white; font-size: 18px; border-radius: 5px;")
        self.descriptionReturn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)  
        self.weatherValue.addRow(self.description, self.descriptionReturn)



    def get_weather(self):

        # apikey df4828bd120132687b91b6e75f59050f

        self.api_key = 'df4828bd120132687b91b6e75f59050f'
        self.city = self.search.text()

        self.params = {'q': self.city, 'appid': self.api_key,'units': 'metric' }

        try:
            url = "http://api.openweathermap.org/data/2.5/weather"
            response = requests.get(url, params= self.params, timeout=10)

        except Exception: 
            pass

        try: 
            if response.status_code == 200:
                    data = response.json()

                    self.cityLabel.setText(f'City Name: {data["sys"]["country"]}: {data["name"]}')

                    self.tempReturn.setText(f'{data["main"]["temp"]} ℃')

                    self.minTempReturn.setText(f'{data["main"]["temp_min"]} ℃ ')

                    self.maxtempReturn.setText(f'{data["main"]["temp_max"]} ℃ ')

                    self.pressureReturn.setText(f' {data["main"]["pressure"]} hPa')

                    self.LatReturn.setText(f'{data["coord"]["lat"]} degrees')

                    self.LongReturn.setText(f'{data["coord"]["lon"]} degrees')

                    # self.descriptionReturn.setText(f'{data["description"]} ')
            else:
                self.cityLabel.setText(f'City Name: Failed to connect to remote Weather API')
        except Exception:
            pass


    def getButtonValue(self):
        city = self.search.text()
        self.cityLabel.setText(f'City Name: {city}')
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myApp = mainUI()
    myApp.show()
    app.exec_()

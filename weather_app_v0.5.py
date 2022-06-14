import sys
import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("ui/we.ui")[0]

class WeatherAppWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("오늘의 날씨")
        self.setWindowIcon(QIcon("icon/1.png"))
        self.statusBar().showMessage('WEATHER APP VER 0.5')

        #날씨 조회 버튼
        self.pushButton.clicked.connect(self.crawling_weather)

    def crawling_weather(self):
        weather_area = self.line.text() # 유저가 입력한 지역텍스트 가져오기
        weather_html = requests.get(f"https://search.naver.com/search.naver?&query={weather_area}날씨")

        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

        area_text = weather_soup.find('h2', {'class': 'title'}).text  # 검색된 날씨 지역명
        print(area_text)

        today_temper = weather_soup.find('div', {'class': 'temperature_text'}).text  # 현재온도
        today_temper = today_temper[6:11]
        print(today_temper)

        yesterday_weather = weather_soup.find('p', {'class': 'summary'}).text  # 어제와의 날씨 비교
        yesterday_weather = yesterday_weather[0:13].strip()  # 13자 까지 가져온 후 공백제거 후 저장
        print(yesterday_weather)

        today_weather = weather_soup.find('span', {'class': 'weather before_slash'}).text  # 오늘날씨
        print(today_weather)

        sense_temper = weather_soup.select('dl.summary_list>dd')
        sense_temper_text = sense_temper[0].text  # 체감온도
        print(sense_temper_text)

        dust_info = weather_soup.select('ul.today_chart_list>li')
        # print(dust_info)
        dust1_info = dust_info[0].find('span', {'class': 'txt'}).text  # 미세먼지 정보
        dust2_info = dust_info[1].find('span', {'class': 'txt'}).text  # 초미세먼지 정보
        print(dust1_info)
        print(dust2_info)

        self.label_2.setText(area_text)
        self.label_3.setText(today_weather)
        self.label_4.setText(today_temper)
        self.label_5.setText(yesterday_weather)
        self.label_9.setText(sense_temper_text)
        self.label_10.setText(dust1_info)
        self.label_11.setText(dust2_info)






# 무한리프
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherAppWindow()
    ex.show()
    sys.exit(app.exec_())
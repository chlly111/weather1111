import sys
import requests
from bs4 import BeautifulSoup

from PyQt5 import uic
# 디자인 만든거 불러와야됨
from PyQt5.QtWidgets import *
#큐티위젯 불러오고
from PyQt5.QtGui import *
#gui 불러오기


#ui 불러와주기
form_class = uic.loadUiType('ui/we.ui')[0]

class WeatherAppWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initWindow()
        #초기화자
        self.setWindowTitle("오늘의 날씨") #타이틀네임
        self.setWindowIcon(QIcon("icon/1.png")) #타이틀사진

    def initWindow(self):
        self.statusBar().showMessage('WEATHER APP VER 0.5 by Hyejin Jang')
        self.show()

        #날씨조회버튼
        self.cc.clicked.connect(self.crawling_weather)


    #크롤링함수설정
    def crawling_weather(self) :
        #weather_area = input('날씨를 알고 싶은 지역으로 입력하세요:(예:서울날씨)')
        # 인풋으로 지역을 받는다.
        weather_area = self.bb.text()  # 유저가 입력한 지역텍스트 가져오기
        weather_html = requests.get(f"https://search.naver.com/search.naver?&query={weather_area}날씨")
        # 쿼리문에 입력될것을 찾는다.
        # print(weather_html.text)
        # weather_html = requests.get(f"https://search.naver.com/search.naver?&query=한남동날씨")
        weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

        area_text = weather_soup.find('h2', {'class': 'title'}).text  # 검색된 날씨 지역명
        print(area_text)

        today_temper = weather_soup.find('div', {'class': 'temperature_text'}).text  # 현재 온도
        print(today_temper[6:10])

        today_temper = today_temper[6:11]
        print(today_temper)

        yesterday_weather = weather_soup.find('p', {'class': 'summary'}).text  # 어제와의 날씨 비교
        print(yesterday_weather)

        yesterday_weather = yesterday_weather[0:13].strip()
        # 공백삭제
        print(yesterday_weather)

        today_weather = weather_soup.find('span', {'class': 'weather before_slash'}).text  # 검색된 날씨 지역명
        print(today_weather)

        sense_temper = weather_soup.select('dl.summary_list>dd')  # 체감온도
        print(sense_temper[0].text)

        sense_temper = sense_temper[0].text
        print(sense_temper)

        dust_info = weather_soup.select('ul.today_chart_list>li')  # 미세먼지
        dust1_info = dust_info[0].find('span', {'class': 'txt'}).text  # 미세먼지
        dust2_info = dust_info[1].find('span', {'class': 'txt'}).text  # 초미세먼지
        print(dust2_info)




        # area_text = self.area_out.text()#지역주소
        # today_temper = self.todayTemper.text()#현재온도
        # yesterday_weather = self.yesterdayWeather.text()#어제날씨와의비교
        # today_weather = self.todayWeather.text()#오늘날씨
        # sense_temper = self.senseTemper.text()#체감온도
        # dust1_info = self.dustWeather1.text()#미세먼지
        # dust2_info = self.dustWeather2.text()#초미세먼지

        self.bb.setText(f"{weather_area}")
        self.ee.setText(f"{area_text}")
        self.gg.setText(f"{today_temper}")
        self.hh.setText(f"{yesterday_weather}")
        self.ff.setText(f"{today_weather}")
        self.jj.setText(f"{sense_temper}")
        self.kk.setText(f"{dust1_info}")
        self.ll.setText(f"{dust2_info}")







# 무한리프
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WeatherAppWindow()
    ex.show()
    sys.exit(app.exec_())
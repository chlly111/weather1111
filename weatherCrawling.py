import requests

from bs4 import BeautifulSoup

weather_area = input('날씨를 알고 싶은 지역을 입력하세요:')

weather_html = requests.get(f"https://search.naver.com/search.naver?&query={weather_area}날씨")
# #print(weather_html.text)0
#weather_html = requests.get(f"https://search.naver.com/search.naver?&query=한남동날씨")

weather_soup = BeautifulSoup(weather_html.text, 'html.parser')

area_text = weather_soup.find('h2',{'class': 'title'}).text #검색된 날씨 지역명
print(area_text)

today_temper = weather_soup.find('div',{'class':'temperature_text'}).text #현재온도

today_temper = today_temper[6:10]

print(today_temper)

yesterday_weather = weather_soup.find('p',{'class':'summary'}).text #어제날씨와 비교
yesterday_weather = yesterday_weather[0:13].strip() #13자 까지 가져온 후 공백제거 후 저장
print(yesterday_weather)

today_weather = weather_soup.find('span',{'class':'weather before_slash'}).text
print(today_weather)

sense_temper= weather_soup.select('dl.summary_list>dd')
sense_temper_text = sense_temper[0].text #체감온도
print(sense_temper_text)

dust_info = weather_soup.select('ul.today_chart_list>li')
#print(dust_info)
dust1_info = dust_info[0].find('span',{'class':'txt'}).text #미세먼지 정보
dust2_info = dust_info[1].find('span',{'class':'txt'}).text #초미세먼지 정보

print(dust1_info)
print(dust2_info)
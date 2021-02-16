# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:31:07 2021

@author: BCBL2
"""

#%% 코드 실행시간 가져오기
"""
import timeit
start = timeit.default_timer() # 시작 시각
stop = timeit.default_timer()
print("time :", stop - start) # 현재시각 - 시작시각 = 코드실행시간
"""

#%% KOSPI, KOSDAQ 지수 불러오기
print(soup.find_all('span', id='KOSPI_now')) # KOSPI
print(soup.find_all('span', id='KOSDAQ_now')) # KOSDAQ
print(soup.find_all('span', id='KPI200_now')) # KOSPI200

print(soup.find_all('span', id='KOSPI_now')[0].text) # KOSPI
print(soup.find_all('span', id='KOSDAQ_now')[0].text) # KOSDAQ
print(soup.find_all('span', id='KPI200_now')[0].text) # KOSPI200


#%% Title table tag
"""
Table Body (tbody) id : gsc_a_b
    tr tag id : gsc_a_tr
        td tag ids :
            gsc_a_t (title)
            <a href = "javascript:void(0)"
            
            data-href = "/citations?view_op=view_citation&hl=en&user=BcXQsQ0AAAAJ&sortby=pubdate&citation_for_view=BcXQsQ0AAAAJ:pQTOvowfQioC"
                class = "gsc_a_at"> <--- 외부 새창 링크 열리면서 나오는 페이지에 대한 class
            
            Inhibitory effects of aloin on TGFBIp-mediated septic responses <--- title of paper
            </a>
        gsc_a_c (cited by)
        gsc_a_y (year)


"""

#%%
#%% (가) Google Scholar Page에서 하나의 논문 제목 불러오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?hl=en&user=BcXQsQ0AAAAJ&view_op=list_works&sortby=pubdate"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

print(soup.find('title'))
level_0 = soup.find('tbody', id='gsc_a_b')
level_1 = level_0.find('tr', class_='gsc_a_tr')
level_2 = level_1.find('a').text
print(level_2)

#%% 모든 제목 불러오기
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?hl=en&user=BcXQsQ0AAAAJ&view_op=list_works&sortby=pubdate"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# url 페이지 제목 확인
print(soup.find('title'))

#%% 논문 제목 단계적으로 찾기 1
level_0 = soup.find('tbody', id='gsc_a_b')

level_1 = level_0.find_all('td', class_='gsc_a_t')

# level_2 = level_1.find_all('a')
# print(level_0)
# print(level_1)
print(level_1)

#%% 2
level_0 = soup.find('tbody', id='gsc_a_b')
level_1 = level_0.find_all('tr', class_='gsc_a_tr')

for i in range (0, 20, 1):
    level_2 = level_1.find('a')

print(len(level_1))
#%%
"""
Feedback
level_2 = level_1.find('a', class_='gsc_a_t') 
--> 'NonType' object has no attribute 'get'

level_2 = level_1.find_all('a')
print(level_2)
---> AttributeError: ResultSet object has no attribute 'find_all'.
     You're probably treating a list of elements like a single element.
     Did you call find_all() when you meant to call find()?

"""
#%%
print(level_1.find_all('a'))
#%% 논문 제목 불러오기

soup.find_all('tr', class_='gsc_a_tr')[0].text
soup.find_all('a', class_='gsc_a_t')[0].text
print(level_2)

# print(soup.find_all('class', id='gsc_a_t')[0].text)
#%% 실습 1
'''
    * 코스피 지수
    * 거래량(천주)
    * 거래대금(백만)
    * 52주 최저 최고 정보 가지고 오기.
'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

print(soup.find('title'))
#%%
# price_now = soup2.find_all('span', class_='blind'))
level_1 = soup2.find('p', class_='no_today')
level_2 = level_1.find('span', class_='blind').text
print(level_2)

dat = soup2.find('p', class_='no_today').find('span', class_='blind').text
print(dat)

#%%
# 코스피 지수
index = soup.find_all('em', id='now_value')[0].text
print("Today's KOSPI :", index)
# 거래량 및 거래대금 가져오기
# 거래량 : td, id: quant
deal = soup.find_all('td', id='quant')[0].text
print("Today's KOSPI :", deal)

# 거래대금 : td, id: amount
deal_money = soup.find_all('td', id='amount')[0].text
print("Today's Dealling amount :", deal_money)

print("execute time :", stop - start)

#%%
kpi_index = soup.find_all('td')
# print(kpi_index)

# 장중 최고
# print("Today's high :", soup.find_all('td')[2].text)
print("Today's high :", kpi_index[2].text)

# 장중 최저
# print("Today's low :", soup.find_all('td')[3].text)
print("Today's low :", kpi_index[3].text)

# 52주 최고
# print("52 weeks' high :", soup.find_all('td')[4].text)
print("52 weeks' high :", kpi_index[4].text)

#52주 최저
# print("52 weeks' low :", soup.find_all('td')[5].text)
print("52 weeks' low :", kpi_index[5].text)

print("execute time :", stop - start)
#%% 실습 2
'''네이버 금융. 현재금액 : 자릿 수 별로 따로 떨어져서 표현돼.
안보이는 태그 확인하고 불러오기

<span class="blind">63,800</span>

'''
from urllib.request import urlopen
from bs4 import BeautifulSoup

url2 = "https://finance.naver.com/item/main.nhn?code=000100"
page2 = urlopen(url2)
soup2 = BeautifulSoup(page2, 'html.parser')

print(soup2.find('title'))

# price_now = soup2.find_all('span', class_='blind'))
level_1 = soup2.find('p', class_='no_today')
level_2 = level_1.find('span', class_='blind').text
print(level_2)

dat = soup2.find('p', class_='no_today').find('span', class_='blind').text
print(dat)
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

#%% title info(1) 논문 제목 단계적으로 찾기
level_0 = soup.find('tbody', id='gsc_a_b')

level_1 = level_0.find_all('td', class_='gsc_a_t')

# print(level_1[0])
# print(level_1[19])

# print(level_1[0].find('a').text)
# print(level_1[19].find('a').text)

for i in range(0, 20, 1):
    print(level_1[i].find('a').text + "\n")

#%% title info(2) 저자 불러오기
auth = level_1[0].find('div', class_='gs_gray').text
# auth = level_1[0].find_all('div', class_='gs_gray')[1].text <---(얘도 된다.)
print(auth)
print(level_1[0].find_all('div', class_='gs_gray')[0].text)
# print(level_1[0].find_all('div', class_='gs_gray')[1].text) : 포맷 구분할 것.

# find는 무조건 첫번째 항만 가져온다.
# div가 여러개일때는 find_all 구문을 추가해주고 뒤에 [n]번호를 붙인다.
"""
Ex) 다음의 다중 div 구문에서,,,
    <div class="class">AAA</div>
    <div class="class">BBB</div>
    
    find 구문
    print(find('div', class_='class')) ---> AAA
    
    find_all 구문
    print(find_all('div', class_='class')[0].text) ---> AAA
    print(find_all('div', class_='class')[1].text) ---> BBB
    
"""

#%% title info(3) 쉼표를 기준으로 출력포맷을 구분하기.
# 출력 포맷에서 저널이름, 수록 페이지 쪽수, 발행년도 분리하기.
jons = level_1[1].find_all('div', class_='gs_gray')[1].text
print(jons)

# 방법 1 : for 구문으로 쉼표 찾고 새로운 문자열 할당 및 join함수로 문자열 결합하기.
"""
# 쉼표의 아스키코드는 44이다. 파이썬에서의 아스키코드 출력은 다음과 같다.
# print(chr(44))

num = len(jons)
jons_name = []

# 출력포맷 문자열에서 쉼표 위치 찾기.
for i in range(0, num, 1):
    jons_name.append(jons[i])
    if jons[i] == chr(44):
        break

print(''.join(jons_name))
"""

# 방법 2 : split 함수로 나누기.(',' : 쉼표를 기준으로 문자열을 나눈다.)
temp_jons = jons.split(',')
pubinfo = temp_jons[0]
# lstrip(), rstrip() 함수는 각기 왼쪽, 오른쪽의 공백을 지운다.
pubpage = temp_jons[1].lstrip()
pubyear = temp_jons[2].lstrip()

print("\nThe name of journal is : ", pubinfo)
print("pages : ", pubpage)
print("published in : ", pubyear)

#%% title info(3-2) Get 'year of published'
yr = level_1[0].find('span', class_='gs_oph').text
print(yr)

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
---> for 구문으로 한개씩 찾아가면 해결!

"""
#%%
print(level_1.find_all('a'))
#%% 논문 제목 불러오기

soup.find_all('tr', class_='gsc_a_tr')[0].text
soup.find_all('a', class_='gsc_a_t')[0].text
print(level_2)

# print(soup.find_all('class', id='gsc_a_t')[0].text)

#%% 엑셀로 데이터 정리.
import pandas as pd

a = [1,2,3,4]
dict = {"회사" : com,
        "코드" : code_p,
        "현재가" : price_c}

dat = pd.DataFrame(dict)
print(dat)

# 엑셀로 만들고 싶다.
dat.to_excel("stock.xlsx", index=False)

# csv a, b, c
dat.to_csv("stock.csv", index=False, encoding='ms949')

#%% 데이터 종합하기 : publish paper 제목, 저자, 저널명, 페이지, 발행년도, (피인용수)
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://scholar.google.com/citations?hl=en&user=BcXQsQ0AAAAJ&view_op=list_works&sortby=pubdate"
page = urlopen(url)
soup = BeautifulSoup(page, 'html.parser')

# url 페이지 제목 확인
print(soup.find('title'))

# init
tit = [] # Title
auth = [] # Author
pubname = [] # Journal
# pubpage = [] # Pages
# pubyear = [] # Year
# cita = [] # Citation

dict = {"Title" : tit,
        "Author" : auth,
        "Journal" : pubname}
        # "Pages" : pubpage,
        # "Year" : pubyear,
        # "Citation" : cita

# Preprocessing
level_0 = soup.find('tbody', id='gsc_a_b')
tit_tmp = level_0.find_all('td', class_='gsc_a_t')


for i in range(0, 20, 1):
    tit.append(tit_tmp[i].find('a').text) # (1) Append title
    auth.append(tit_tmp[i].find('div', class_='gs_gray').text) # (2) Append Authors
    
    jons = tit_tmp[i].find_all('div', class_='gs_gray')[1].text # Get publication info
    temp_jons = jons.split(',') # split info to ','
    pubname.append(temp_jons[0]) # (3) Get Journal name
    
    """
    title 항목에서는 수록 페이지 수와 발행년도가 미확인 되는 경우가 생김.
    [11]논문: div class="gs_gray" 태그 내용: 2개.(페이지 없음)
    저널이름은 pubname에 append되는데 문제 없음. 페이지 정보가 없으므로 pubpage에 발행년도 2020이 append됨.
    pubpage for 구문이 돌고 나면, pubyear에 year을 할당해야하는데, [11]논문의 2020이 pubpage에 할당되는 바람에 다음의 오류가 생성
    ---> IndexError : list index out of range
    
    수록 페이지 수는 어디서 크롤링 하면 될까? 없으면 패스하도록 개선해야.
    발행년도는 Title(class_='gsc_a_t)이 아닌 year(class_='gsc_a_y')에서 크롤링하면 된다.
    """
    # pubpage.append(temp_jons[1].lstrip()) # (4) Get pages
    # pubyear.append(temp_jons[2].lstrip()) # (5) Get publication year
    
    
# print(tit)
# print(auth)
# print(pubname)
# print(pubpage)
# print(pubyear)

import pandas as pd
# import openpyxl
# 'openpyxl' imported but unused

df = pd.DataFrame(dict)
# print(dat)

# 엑셀로 만들고 싶다.
df.to_excel('C:/Users/SIMHYUNCHAE/Documents/GitHub/meta_bcblpap/gsc1-20.xlsx', index=False)

# to csv a, b, c
# dat.to_csv("stock.csv", index=False, encoding='ms949')


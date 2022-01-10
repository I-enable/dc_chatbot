import requests
from bs4 import BeautifulSoup
import time
import random
from var_name import USER_AGENT


wakmagall = "https://gall.dcinside.com/mgallery/board/lists?id=wackgood"
isedol = "https://gall.dcinside.com/mgallery/board/lists?id=leesedol"
def uurl():
    global html_list
    
    url = wakmagall
    headers = USER_AGENT
    res = requests.get(url, headers=headers) 
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    html_list = soup.find('tbody').find_all('tr')

idx = 0
value = 0
num = 0
crol = 10
stopper = 0

# 시간변수
timeset = [5, 5.5, 6, 6.5, 7]

# 제목 크롤링
def chat():
    global idx
    global title_list
    global number_list
    global num
    
    for i in reversed(html_list):
        title_list = i.find('a').text
        number_list = i.find("td", attrs={"class":"gall_num"}).text
        idx += 1
        
        if idx > 30 and idx < 46:
            number_list = int(number_list)
            
            if number_list > num:
                print(title_list)
                num = number_list
                # print(num)
            
            
# 실행코드
while value < 100:
    uurl()
    chat()
    idx = 0
    time.sleep(random.choice(timeset))
    value += 1
    if value == crol:
        print("[현재 크롤링 {}회]".format(crol))
        crol = crol + 10
        


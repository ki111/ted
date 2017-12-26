# coding: UTF-8
import urllib2
from bs4 import BeautifulSoup
import time

# 変数準備
url = "https://www.ted.com/talks?page="
total_page = 74 
count =0
file = open('ted-link.csv','w')
file.write("#,link\n")

# スクレイビング
for page_num in range(total_page):

    # URLにアクセス、取得したページをBeautifulsoupに格納し解析準備
    html = urllib2.urlopen(url+str(page_num))
    soup = BeautifulSoup(html, "html.parser")
    
    # 進捗確認のため現ページ数を表示
    print(page_num)

    # 過剰アクセスを防ぐため5秒休憩
    time.sleep(5)
    
    # プレゼンへのリンクを取得
    for link in soup.find_all(class_=" ga-link"):
        count = count + 1
    
        #1プレゼン当たり画像とタイトル計2個のリンクがあるため重複を防ぐ
        if count % 2 == 0:
            file.write(str(count/2)+","+link.get('href')+","+"\n")
        
file.close()
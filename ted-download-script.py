# coding: UTF-8
from selenium import webdriver
from bs4 import BeautifulSoup
from datetime import datetime
import time
import pandas
import numpy

# 変数準備
url = "https://www.ted.com"
csv = pandas.read_csv('ted-link.csv')
page = 0

# SeleniumよりChromeを立ち上げる
browser = webdriver.Chrome()

# スクレイビング開始
for link in csv["#"]:
    
    # プレゼン毎に格納ファイルを準備
    file = open('./content/'+str(page)+'.html','w')

    # プレゼンにアクセス
    browser.get(url+str(link)+"/transcript")
    page = page + 1
    
    # Javascript読み込みが完了を待つため5秒休憩
    time.sleep(5)
    
    # ページ内容を取得、Beautifulsoupに格納し解析準備
    html_source = browser.page_source
    soup = BeautifulSoup(html_source, "html.parser")

    # 英文スクリプト要素を準備したファイルに書き込み
    for content in soup.find_all(class_="t-d:n hover/bg:gray-l.5"):
        file.write(str(content.get_text())+" ")
    
    
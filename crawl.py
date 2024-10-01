import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_top_10_stocks():
    url = 'https://finance.naver.com/sise/sise_rise.naver?sosok=1' 
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.select_one('#contentarea > div.box_type_l > table')
        rows = table.find_all('tr')

        cnt = 10
        stocks = []
        for row in rows:
            if cnt == 0: break
            res = row.find('a', class_='tltle')
            if res:
                cnt -= 1
                stocks.append((res.text.strip(), "finance.naver.com" + res.get('href')))

        return stocks
        
    return response.status_code


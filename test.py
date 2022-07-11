import requests
from bs4 import BeautifulSoup as BS
import lxml
class Parser:
        def __init__(self):
                pass

        def parse(URL):
                HEADERS = {
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
                }
                response = requests.get(URL, headers=HEADERS)
                soup = BS(response.content, 'lxml')
                item = soup.find('table', class_='text').get_text()
                return item







import requests
#import Options
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver

#options = Options()
#options.add_argument("--lang=en")
#driver = webdriver.Safari()

instagram_URL = 'https://www.instagram.com'
profile_URL = 'paoloangeles'
response = requests.get(f"{instagram_URL}/{profile_URL}")
print(response.status_code)
if response.ok:
    print(response.text)

# headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}

# page = requests.get(URL, headers = headers)

# soup = BeautifulSoup(page.content, 'html.parser')
# soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

# print(soup2.prettify())
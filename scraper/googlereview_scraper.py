

import requests
import Options
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver

options = Options()
options.add_argument("--lang=en")
driver = webdriver.Safari()

URL = 'https://www.google.com/maps/place/The+Sandwich+Bar/@51.2680777,0.4975328,17z/data=!3m1!4b1!4m7!3m6!1s0x0:0xce24c9bad316fbcd!8m2!3d51.2680777!4d0.4997215!9m1!1b1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(soup.prettify(), 'html.parser')

print(soup2.prettify())
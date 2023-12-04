import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.wizardingworld.com/discover/books").text

soup = BeautifulSoup(html, "lxml")


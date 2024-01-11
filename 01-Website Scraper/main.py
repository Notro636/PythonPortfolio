import requests
import xml
from bs4 import BeautifulSoup

URI = ""
page = requests.get(URI)

soup = BeautifulSoup(page.content, "html.parser")
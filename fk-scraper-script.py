from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree
from bs4 import BeautifulSoup
import datetime


show_date = input('Anna päivämäärä: ')

url = 'https://www.finnkino.fi'
post_fields = {
    'blockID': '4571',
    'TheatreArea': '1035',
    'dt': show_date,
    'orderBy': 'showTime',
    'order': 'asc',
    'X-Requested-With': 'XMLHttpRequest',
    'updateTargetId': 'UpdateTarget-UserControlScheduleGroupShowList_102'
}

request = Request(url, urlencode(post_fields).encode(),headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(request).read().decode()
soup = BeautifulSoup(html, "html.parser")

# find all movies in soup
for titleInfo in soup.find_all("div", {"class": "show-list-item"}):
    eventName = titleInfo.find(
        'h1', {'class': 'eventName'}).find('a').text.strip()
    showTime = titleInfo.find('h2', {'class': 'showTime'}).text.strip()
    showLocation = titleInfo.find(
        'h4', {'class': 'showLocation hidden-xs hidden-sm'}).text.strip()
    print(eventName+', '+showTime+', '+showLocation)
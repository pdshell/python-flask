# -*- coding: utf-8 -*-
import urllib.request
import urllib
import re
import requests as req
from bs4 import BeautifulSoup

url = "https://www.mytoken.io/"
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
})
response = urllib.request.urlopen(req)
content = response.read()

# print(content)

# pageFile = open('pageCode'.replace('/', '_') + ".html", 'wb')  # 以写的方式打开pageCode.txt
# pageFile.write(content)  # 写入
# pageFile.close()

# resp = re.compile(r'src="(.+?\.jpg)" width')
# img_list = resp.findall(content)
# print(img_list)


# resp = re.compile(r'src="(.+?\.jpg)" width')
# rsp = req.get(url)
# html = rsp.text
# print(resp.findall(html))

# html = str(BeautifulSoup(html, "lxml"))
# print('bs4Soup:\t', resp.findall(html)[0])

#!/usr/bin/python python
# -*- coding:utf-8 -*-
import urllib
import urllib2,cookielib
from bs4 import BeautifulSoup


response =  urllib2.urlopen("https://www.zhihu.com")

url = "https://www.zhihu.com/#signin"
text = response.read()
soup = BeautifulSoup(text,'html.parser',from_encoding="utf8")
_xsrf = soup.find("input",{"name":"_xsrf"})
print(_xsrf["value"])

headers = {
    "User_Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate, sdch",
    "Referer":"https://www.zhihu.com/"
    }
cookieJar = cookielib.CookieJar()
handle = urllib2.HTTPCookieProcessor(cookieJar)
opener = urllib2.build_opener(handle)
urllib2.install_opener(opener)



#_xsrf = BeautifulSoup(urllib2.urlopen(url).read(),'html.parser',from_encoding="utf-8").find("input",{"name":"_xsrf"})["value"]

loginparameters = {'_xsrf':_xsrf["value"],'username':"zhixiangchai@163.com",'passwd':"czx88888"}




request = urllib2.Request(url,urllib.urlencode(loginparameters),headers=headers,)
response = urllib2.urlopen(request)

print response.read()

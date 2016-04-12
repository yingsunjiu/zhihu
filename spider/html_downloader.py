#!/usr/bin/python python
# -*- coding:utf-8 -*-
import urllib2,cookielib


class HtmlDownloader(object):

    headers = {"User_Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64)"}
    cookieJar = cookielib.CookieJar()
    handle = urllib2.HTTPCookieProcessor(cookieJar)
    opener = urllib2.build_opener(handle)
    urllib2.install_opener(opener)

    def download(self,url):
        if url is None:
            return
        request = urllib2.Request(url,headers=self.headers)
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        return response.read()



#-*- coding:utf-8 -*-
import urllib
import urllib2
url = 'http://hda.yiche.com/tool/Home/Index/login'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}
values = {}
values['username'] = 'hdadminmaster'
values['password'] = 'hdyiche654321'
data = urllib.urlencode(values)
print data
request = urllib2.Request(url,data,headers=headers)
response = urllib2.urlopen(request)
print response.read()

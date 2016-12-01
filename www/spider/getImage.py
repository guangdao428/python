#-*- coding:utf-8  -*-
import urllib
import re
import os

def getHtml(url):
	page = urllib.urlopen(url)
	html = page.read()
	return html

def getImage(html):
	reg = r'src="(http.*?\.jpe?g)"\s*class';
	reg = re.compile(reg)
	imglist = re.findall(reg,html)
	#print imglist
	for imgurl in imglist:
		print os.path.split(imgurl)
		urllib.urlretrieve(imgurl,os.path.join('static/img/',os.path.split(imgurl)[1]))
		print 'ok'


html = getHtml('http://image.baidu.com/');
imglist = getImage(html)


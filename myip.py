#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/9 2:00 下午
# @Author  : Tang Jiuyang
# @Site    : https://tangjiuyang.com
# @File    : myip.py
# @Software: PyCharm
import urllib.request

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url='http://ip.cn', headers=headers)
text = urllib.request.urlopen(req).read()
print(str(text,'utf-8'))

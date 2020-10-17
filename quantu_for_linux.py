#!/user/bin/python
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os
import time
import _thread
categaries = {}
person = {}
items = {}
log = []
PATH = os.getcwd()
forbidchar = r'<|>|/|\\|\||:|"|\*|\?'
page_list=[]
package_list=[]

def downloadimg(link, name):
	name = re.split(forbidchar, name)
	name = '.'.join(name)
	for i in range(1):
		#time.sleep(0.5)
		try:
			data = urlopen(link, timeout=10)
			tname = name+".jpg"
			with open(tname, "ab") as code:
				code.write(data.read())
			print(tname+" is done.")
		except Exception:
			time.sleep(3)
	else:
		return False
	return True

def page(link):
	page_list = [link]
	for i in range(10):
		try:
			html = urlopen(link, timeout=10)
			break
		except Exception:
			print("Url Erroe")
            #time.sleep(2)


	try:
		bsObj = BeautifulSoup(html, "html.parser")
	except Exception:
		print("Soup Error")
	try:
		for center in bsObj.findAll("div",{"class":"c_page"}):
            #print(center)
			for a in center.findAll("a"):
                #print('http://www.quantuwang.co'+str(a.attrs['href']))
				llink = 'http://www.quantuwang.cc'+str(a.attrs['href'])
				page_list.append(llink)
                    #for url in page_list:
             #   downloaditem(url)
	except:
		pass

	return page_list
    #print(page_list)
	'''
    downloaditem_1(page_list[0])
    for urll in page_list[1:]:
        downloaditem(urll)
	'''


def downloaditem(link, ):
		#time.sleep(1)
	for i in range(10):
		try:
			html = urlopen(link)
			break
		except Exception:
			print("Url Erroe")

	for i in range(10):
		try:
			bsObj = BeautifulSoup(html, "html.parser")
			a = 0
			break
		except Exception:
			print("Soup Error")
			a = 1

	if a == 0:       
		try:
			for center in bsObj.findAll("div",{"class":"c_img"}):
            	#print(center)
				for img in center.findAll("img"):
					#boola = downloadimg(img.attrs['src'], img.attrs['alt'])
					#my_dict = {"name": "小明", "age": 18, "no": "007"}
					download_name=str((img.attrs['alt']))
					download_link=str((img.attrs['src']))

		except:
			pass
		return [download_name,download_link]

def downloadperson(link):

	html = urlopen(link, timeout=10)          # 打开链接
	bsObj = BeautifulSoup(html, "html.parser") # 用bs解析

	package_list = []
	for boxs in bsObj.findAll("div", {"class":"index_left"}): # 找到装载图片集的<div>标签
        #print(boxs)
		for li in boxs.findAll("li"):   
            #print(li)                # 处理每一个图片集
			for a in li.findAll('a'): # 找到包含图片链接的p标签
                #print(a.attrs['href'])
                #psn = p.find('a')
				package_list.append('http://www.quantuwang.cc'+str(a.attrs['href'])) # 用文件名作为key给字典添加图集链接
    #print(package_list)
	#for package in package_list:
	#	page(package)
	return package_list
            
#def download_new(i):
#	downloadimg(download_urls[i],download_names[i])
'''
#downloaditem('http://www.quantuwang.co/m/6ed55b315bff6ad3.html')
page('http://www.quantuwang.co/m/50fa25ee319ffc0e.html')
#downloaditem_1('http://www.quantuwang.co/m/50fa25ee319ffc0e.html')
'''
PACKAGE_NUM = 1
tmp_num = int(PACKAGE_NUM)
while tmp_num != 0:
	#THE_PERSON = input("Enter the url: ")
	THE_PERSON = "http://www.quantuwang.cc/t/e4d09316d8a9d330.html"
	package_list = package_list + downloadperson(THE_PERSON)
	tmp_num = tmp_num-1
#package_list = downloadperson('http://www.quantuwang.co/t/ddcc0f5bf2efada3.html')
#print(package_list)
summ = len(package_list)
a = summ//5
b = a * 2
c = a * 3
d = a * 4
e = summ - 1

def threads(s,e):
	for package in package_list[s:e]:
		#图集首页以捕捉全部页面
		try:
			pagelist = page(package)
			temp = downloaditem(pagelist[0])
			#print(temp[0])
			#print(temp[1])
			tempo_n = str(temp[0])[:-3]
			tempo_l = str(temp[1])[:-5]
			#print(tempo_l)
			#print(tempo_n)
			download_urls= []
			download_names= []

			for i in range(len(pagelist)):
				tempor_l = tempo_l + str(i+1) + '.jpg'
				tempor_n = tempo_n + str(i+1)
				#print(tempor_l)
				#print(tempor_n)
				download_urls.append(tempor_l)
				download_names.append(tempor_n)
				#print(download_urls)
				#print(download_names)
			print("Form finished!")

			#download_new(0)
			for k in range(len(pagelist)):
				downloadimg(download_urls[k],download_names[k])
		except:
			pass
	
#threads(0,5)

try:
	_thread.start_new_thread( threads, (0,a,) )
	_thread.start_new_thread( threads, (a,b,) )
	_thread.start_new_thread( threads, (b,c,) )
	_thread.start_new_thread( threads, (c,d,) )
	_thread.start_new_thread( threads, (d,e,) )
except:
	print ("Error: 无法启动线程")


t = 120000
while t > 0:
	time.sleep(1)
	t = t - 1
	pass






import requests,time,os,json
from requests import Session

import sys


def phone():
	send = Session()
	phonee = input("namber > ")
	send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
	snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{phonee[1:]}")
	sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
	y = input("อีกรอบไหม/y : ")
	if (y == "y"):
		phone()
		
	
	else:
		print ("Bye ! ")
		
		

	
phone()

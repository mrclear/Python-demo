import re
import urllib
import urllib2

url1="http://www.5442.com/meinv/20150123/13877_"
imgnum=0
i=0
while i<16:
    i+=1
    url=url1+str(i)+".html"    
    page=urllib.urlopen(url)
    html=page.read()
    reg=r"src='(.*?\.jpg)'"
    imgre=re.compile(reg)
    imglist=re.findall(imgre,html)
    
    for imgurl in imglist:
        urllib.urlretrieve(imgurl,'%s.jpg'%imgnum)
        imgnum+=1

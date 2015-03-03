from BeautifulSoup import BeautifulSoup
import urllib2
import re

inputmsg=raw_input("Enter search term:")
url1=""
for i in inputmsg.split():
    url1=url1+i+"+"
url2=url1[:-1]
urlsearch="http://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText="+url2
tempurl="http://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText=natural+language+processing+cloud+computing"
html_page=urllib2.urlopen(urlsearch)
soup=BeautifulSoup(html_page)
links=[]

for link in soup.findAll('a'):
    links.append(link.get('href'))

for i in links:
    if i!=None:
        if i[:12]=="/xpl/article":
            print "http://ieeexplore.ieee.org"+i
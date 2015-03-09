from BeautifulSoup import BeautifulSoup
import urllib2

input_msg = raw_input("Enter search term:")
url1 = ""
for i in input_msg.split():
    url1 = url1+i+"+"
url2 = url1[:-1]
url_search = "http://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText="+url2
temp_url0 = "http://ieeexplore.ieee.org/search/searchresult.jsp?"
temp_url = temp_url0 + "newsearch=true&queryText=natural+language+processing+cloud+computing"
html_page = urllib2.urlopen(url_search)
soup = BeautifulSoup(html_page)
links = []

for link in soup.findAll('a'):
    links.append(link.get('href'))

for i in links:
    if i is not None:
        if i[:12] == "/xpl/article":
            print "http://ieeexplore.ieee.org"+i
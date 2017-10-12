from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_38519.html'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


tags = soup('span')

total = 0

for span in tags:
	x = (int(span.string))
	total += x

print (total)

#based on urllinks.py from 'Python for Everyone'

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL: ')
keyword = input('Enter a keyword: ')

try:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

#Retrieve all of the anchor tags
    tags = soup('a')
    for tag in tags:
        url = tag.get('href', None)
        #print(url)
        if keyword in url: #only select urls related to keyword
            print(url)
        else:
            print('No match found.')

except:
    print('Invalid URL. Please try again.')

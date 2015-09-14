#!/usr/bin/python

import json
import urllib
import urllib2

jsonResponse = json.loads(
    urllib2.urlopen('http://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US').read())

imageUrl = jsonResponse['images'][0]['url']

# download the image and once it's downloaded, we will write it to an image
imageUrl = "http://www.bing.com" + imageUrl
imageFile = open("{***put your preferred directory here****}/bing-daily-backgorund.jpg", "wb")
imageFile.write(urllib.urlopen(imageUrl).read())
imageFile.close()

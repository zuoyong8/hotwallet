from itertools import count
import ujson
import base64

from configobj import ConfigObj
from pycurl import Curl #sudo apt-get install libcurl4-openssl-dev for ubuntu

try:
	import urlparse
except：
    from urllib import parse as urlparse

try:
	from cStringIO import StringIO
except:
	try:
		from StringIO import StringIO #python2.x
	except:
		from io import StringIO #python3.x


class ServiceProxy(object):
    def __init__(self,url,port,conf_file)
        pass

    def __getattr__(self,attr):
    	pass

    


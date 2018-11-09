import sys, os
from pycurl import Curl
try:
    from StringIO import StringIO
except:
	from io import  StringIO


# curl = Curl()
# fs = StringIO()
# fs.write('First line\n')
# print('second line\n',file=fs)
# contents = fs.getvalue()
# print(contents)
# curl.setopt(curl.URL,"http://www.baidu.com")
# curl.setopt(curl.WRITEFUNCTION,fs.write)
# curl.setopt(curl.MAXREDIRS,5)
# curl.setopt(curl.CONNECTTIMEOUT,60) #链接超时
# curl.setopt(curl.USERAGENT,'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)')
# curl.perform()
# print("HTTP-code:", curl.getinfo(curl.HTTP_CODE))
# fs.close()
# curl.close()
class Proxy(object):
	def __init__(self,url=None):
		self.conn = 'cc'
		print('__init__')

	def __getattr__(self,method):
		result = 'attr'
		def call(*params):
			return 'bbb'
		return result

p = Proxy()
# print(p.result)
print('work flow')
print('master')
print('develop')
print('feature')
print('release')
print('hotfix')
		



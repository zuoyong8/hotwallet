import pytest
from configobj import ConfigObj
# import ConfigParser

def test_config():
	co = ConfigObj('bitcoin.conf')
	assert co['rpcuser']=='bitcoin'
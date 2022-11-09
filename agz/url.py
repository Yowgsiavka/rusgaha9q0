from secrets import choice
from socket import socket
from requests import get
class Url:
	
	_socket = "wss://shsocket9.iranlms.ir:80"
	_api = "https://shadmessenger139.iranlms.ir/"
	_storange = "https://shstorage527.iranlms.ir/"
	
	def data():
		urls = get('https://shgetdcmess.iranlms.ir/').json()
		return urls['data']
	
	def socket():
		urls = Url.data()['socket']
		return list(urls.values())[0]
		
	def api():
		urls = Url.data()['API']
		return list(urls.values())[0]
		
	def storage():
		urls = Url.data()['storage']
		return list(urls.values())[0]
		
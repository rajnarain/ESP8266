import socket
import network
import gc
gc.collect()
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config('MicroPython-AP--', password= '12345678')

while ap.active() == False:
	pass

print('Connection successful')
print(ap.ifconfig())

def web_page():
	html = """<html><h1>Hello, World!</h1></html>"""
	return html

s = socket.socket()
s.bind(('', 80))
s.listen(5)


while True:
 	conn, addr = s.accept()
  	print('Got a connection from %s' % str(addr))
  	request = conn.recv(1024)
  	print('Content = %s' % str(request))
  	response = web_page()
  	conn.send(response)
  	conn.close()


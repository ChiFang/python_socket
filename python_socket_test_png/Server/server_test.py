# server  

import sys
import socket  

########## init socket setting ##########
print '--------------------'
print ("init socket setting...")
import ConfigParser
Config = ConfigParser.ConfigParser()

Config.read("ClientCFG.ini")

# list all sections
Config.sections()

# get as string
ip = Config.get('socket', 'server_IP')

# get as number
port = Config.getint('socket', 'port')

# get as number
DataSize = Config.getint('data', 'image_size')

# get as boolean
repeat = Config.getboolean('mode', 'repeat')

print ("server IP: " + ip)
print ("port: " + str(port))
print ("image size: " + str(DataSize))
print ("repeat: " + str(repeat))
print '--------------------'
########## init socket setting ##########


########## image transfer by socket ##########
print ("image transfer by socket...")
DataSizeStr = 512
address = (ip, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sock = socket.socket()  
sock.bind(address)  
sock.listen(5)

print 'waiting for a connection...'

connection, client_address = sock.accept()

print 'got connected from',client_address

connection.send('Server: Ready to receive data...')  

print ("receive data.......")
data = connection.recv(DataSize)

print ("data size: " + str(len(data)) + " (byte)")

if len(data)<DataSizeStr:	#no data quit
	print ("Quit this program~~~")
	connection.send("No data Quit~~~")
	connection.close()  
	sock.close()
else:	#start calculating
	file_out = open('tmp_1.png', 'wb')

	print 'writting file...'
	file_out.write(data)
	file_out.close()
	print 'writting file finish...'
########## image transfer by socket ##########


connection.send('Server: end of calculating')
sock.close()
	


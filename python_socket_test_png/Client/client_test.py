# client  
  
import socket  
  
########## init socket setting ##########
print ("init socket setting...")
import ConfigParser
Config = ConfigParser.ConfigParser()

Config.read("../Server/ClientCFG.ini")

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
########## init socket setting ##########

address = (ip, port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sock = socket.socket()  
sock.connect(address) 

print '--------------------'
data = sock.recv(512)  
print data  
file = open('Input_8.png', 'rb')
content = file.read()
file.close()
print 'content size is ', len(content)  
sock.send(content)
print 'content transfer is done.'
print ("calculating....")
data = sock.recv(512)  
print data
print '--------------------'
  
sock.close()

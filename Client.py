# Import socket module 
import socket, json, pickle
import time, sys             
  
# Create a socket object 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)          

#the argument after filename will be the ip address of the server
host = sys.argv[1]

#second argument is the port number
port = int(sys.argv[2])
  
# connect to the server on local computer 
s.connect((host, port))

#opening a file
with open('input.dat') as fp:
	line = fp.readline()
	
	while line:
	#arr = [1,2,3]
		arrayToSend = []
		for item in line.strip().split(","):
			arrayToSend.append(item)
		#print arrayToSend
		data_string = json.dumps(arrayToSend)
		s.send(data_string)

		art = s.recv(4096)
		#data_arr = json.loads(art)
		#print type(data_arr)
		time.sleep(2)
		line = fp.readline()
		print 'Sorted array received from the server ', art
s.close()



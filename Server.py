
# import the socket library 
import socket
import json, pickle
import os, sys           



#merge sort
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        mergeSort(L) # Sorting the first half 
        mergeSort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1
    return arr   	


# next create a socket object 
s = socket.socket()        
count =0  
print "Socket successfully created"
  
# take port number as input                
port = int(sys.argv[1])

# Next bind to the port 
# we have not typed any ip in the ip field 
# instead we have inputted an empty string 
# this makes the server listen to requests  
# coming from other computers on the network 
s.bind(('', port))         
print "socket binded to %s" %(port) 
  
# put the socket into listening mode 
s.listen(5)      
print "socket is listening...."            
  
# a forever loop until we interrupt it or  
# an error occurs 
while True: 

	# Establish connection with client. 
	c, addr = s.accept()      
	print 'Got connection from', addr 
	count= count+1
	pid=os.fork()
	if (pid)==0:

		print "New child created for client request with number ", count
		s.close()

		while True:
			data = c.recv(4096)
			recievedArray = data.strip('[]').replace("\"","")
			sortingArray = []
			for item in recievedArray.split(","):
				sortingArray.append(item)
			#print "tobesend ", sortingArray
			sorted = mergeSort(sortingArray)
			if not data:
				#print "no data condition"
				break
			c.send(json.dumps(sorted))
		os. _exit(0)
		pid,status = os.waitpid(0,WNOHANG)
	
	
	
# Close the connection with the client 
c.close()




# import socket module
from socket import *
import threading
# In order to terminate the program
import sys
#finding ipaddress
hostname = gethostname()
ipaddress = gethostbyname(hostname)
portNumber=6754

def client(connectionSocket,addr):
    
    try:
        
        message = connectionSocket.recv(1024)### YOUR CODE HERE ###

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() ### YOUR CODE HERE ###

        # Send one HTTP header line into socket
        ### YOUR CODE HERE ###
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file into socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close client socket
        connectionSocket.close()
        
    
    except IOError:
        # Send response message for file not found
        ### YOUR CODE HERE ###
        connectionSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n","utf-8"))
        connectionSocket.send(bytes("<html><head></head><body><h1><FONT COLOR=RED>404 Not Found</h1></body></html>\r\n","utf-8"))

        # Close client socket
        ### YOUR CODE HERE ###
        connectionSocket.close()
       # Close server socket

def main():
# Prepare a sever socket
    serverSocket = socket(AF_INET, SOCK_STREAM)
    ### YOUR CODE HERE ###

    serverSocket.bind((ipaddress, portNumber))

    serverSocket.listen()

    while True:
        # Establish the connection
        print('Ready to serve...')
    

        connectionSocket, addr = serverSocket.accept() ### YOUR CODE HERE ###
        
        thread = threading.Thread(target=client, args=(connectionSocket,addr))
        
        
        thread.start()

    # Close server socket
    serverSocket.close()

    # Terminate the program after sending the corresponding data
    sys.exit()


        
if __name__ == "__main__":
    main()  

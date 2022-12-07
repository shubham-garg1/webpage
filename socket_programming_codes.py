
### Client connects to the server, recieves text from server and displays it


# Client:
import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((socket.gethostname(), 25000))

msg = clientsocket.recv(1024)
print(msg.decode())
clientsocket.close()


# Server:
import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 25000))
serversocket.listen()
connection, address = serversocket.accept()

print("Connection has been established")
message = "Hello Client!"
connection.send(message.encode())
connection.close()
serversocket.close()

"""### Client sends array, server sends min and max."""

# Client
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.connect((host, port))
data = [1, 2, 3, 4, 5]
s.sendall(data)
min_element, max_element = s.recv(1024)
s.close()
print(f"Minimum element: {min_element}")
print(f"Maximum element: {max_element}")

# Server
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 9999
s.bind((host, port))
s.listen()
while True:
    clientsocket, addr = s.accept()
    print(f"Got a connection from {addr}")
    data = clientsocket.recv(1024)
    min_element = min(data)
    max_element = max(data)
    clientsocket.sendall((min_element, max_element))
    clientsocket.close()

"""### Chat application between Client and server that runs till client sends "bye"."""

# Client:
import socket

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()




# Server:
import socket

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    server_socket.listen()
    conn, address = server_socket.accept()  # accept new connection
    print(conn)
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

if __name__ == '__main__':
    server_program()

"""# Lab Manual Questions:

### Write a TCP client program which reads a sentence from the user and sends it to the TCP server program which converts it into uppercase and sends the result back to the client program which displays the result. (Expt 7)
"""

# Client:

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:
    message = input('Enter a message to send: ')
    print('sending {!r}'.format(message))
    sock.sendall(message.encode())
    data = sock.recv(1024)
    print('received {!r}'.format(data.decode()))

finally:
    print('closing socket')
    sock.close()



# Server:

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        data = connection.recv(1024)
        print('received {!r}'.format(data.decode()))
        response = data.upper()
        connection.sendall(response)
    finally:
        connection.close()

"""### In python, write client and server codes for socket programming. A UDP client program reads a sentence from the user and sends it to the UDP server program which converts it into uppercase and sends the result back to the client program which displays the result. (Expt 8)"""

# Client:

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
try:
    message = input('Enter a message to send: ')
    print('sending {!r}'.format(message))
    sent = sock.sendto(message.encode(), server_address)
    print('waiting to receive')
    data, server = sock.recvfrom(4096)
    print('received {!r}'.format(data.decode()))
finally:
    print('closing socket')
    sock.close()


# Server:

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
while True:
    print('\nwaiting to receive message')
    data, address = sock.recvfrom(4096)
    print('received {} bytes from {}'.format(len(data), address))
    print(data.decode())
    response = data.upper()
    sock.sendto(response, address)

"""### Write a TCP client program which connects to TCP server program and reads a file content which is sent by the server program and writes into a newly created file. (Expt 9)"""

# Client:

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
try:
    data = sock.recv(1024)
    with open('received_file.txt', 'wb') as f:
        f.write(data)
finally:
    print('closing socket')
    sock.close()


# Server:

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        with open('file_to_send.txt', 'rb') as f:
            data = f.read()
        connection.sendall(data)
    finally:
        connection.close()

"""### Write a TCP client program which reads two integers from the user and passes them to the TCP server program which adds them and sends the result back to the client which displays the result (Expt 10)"""

# Client:
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)
try:
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    message = '{},{}'.format(num1, num2)
    print('sending {!r}'.format(message))
    sock.sendall(message.encode())
    data = sock.recv(1024)
    print('received {!r}'.format(data.decode()))
finally:
    print('closing socket')
    sock.close()



# Server:
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(1)
while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)
        data = connection.recv(1024)
        print('received {!r}'.format(data.decode()))
        num1, num2 = map(int, data.split(','))
        result = num1 + num2
        response = str(result)
        connection.sendall(response.encode())
    finally:
        connection.close()

# Client:
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9999
s.connect((host, port))                               
# read two integers from the user
num1 = int(input("Enter first integer: "))
num2 = int(input("Enter second integer: "))
# send the two integers to the server
s.sendall(str(num1).encode('ascii'))
s.sendall(str(num2).encode('ascii'))
result = s.recv(1024)   # receive the result from the server                       
s.close()
print("The result is:", result)



# Server:
import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
host = socket.gethostname()                           
port = 9999
serversocket.bind((host, port))                                  
serversocket.listen(5)                                           
while True:
    clientsocket,addr = serversocket.accept()      
    print("Got a connection from %s" % str(addr))
    # receive the two numbers from the client
    num1 = int(clientsocket.recv(1024))
    num2 = int(clientsocket.recv(1024))
    # add the two numbers and send the result to the client
    result = num1 + num2
    clientsocket.send(str(result).encode('ascii'))
    clientsocket.close()
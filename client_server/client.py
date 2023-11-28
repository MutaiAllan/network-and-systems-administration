import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 12345)
client_socket.connect(server_address)
print("Connected to {}:{}".format(*server_address))

# Send a request to the server
request = "Hello, server! How are you?"
client_socket.send(request.encode('utf-8'))
print("Sent request to server: {}".format(request))

# Receive the response from the server
response = client_socket.recv(1024)
print("Received response from server: {}".format(response.decode('utf-8')))

# Close the connection
client_socket.close()

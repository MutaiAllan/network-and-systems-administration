import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections (maximum of 1 connection in this example)
server_socket.listen(1)
print("Server is listening on {}:{}".format(*server_address))

# Wait for a connection from a client
print("Waiting for a connection...")
client_socket, client_address = server_socket.accept()
print("Accepted connection from {}:{}".format(*client_address))

# Receive data from the client
data = client_socket.recv(1024)
print("Received data from client: {}".format(data.decode('utf-8')))

# Send a response back to the client
response = "Hello, client! This is the server."
client_socket.send(response.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()

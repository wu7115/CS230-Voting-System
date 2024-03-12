import socket
import pickle
import ntplib
from time import ctime

server_list = [0, 0, 0]

# Server configuration
host = '172.31.5.39' # master private IP
port = 15469
# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))
# while(1):
for i in range(5):

    # Listen for incoming connections
    server_socket.listen()

    print(f"Server listening on {host}:{port}")

    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive the list from the client
    data = client_socket.recv(1024)

    received_list = pickle.loads(data)

    # Update the server's list
    for i in range(len(received_list)):
        server_list[i] += received_list[i]

    # Print out the updated list
    print(f"Updated list on the server: {server_list}")
    
# Close the connection
# client_socket.close()
# server_socket.close()
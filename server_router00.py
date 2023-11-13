import socket
import time

# Server settings
UDP_IP = "0.0.0.0"
UDP_PORT = 55055

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind((UDP_IP, UDP_PORT))

print(f"Server started on {UDP_IP}:{UDP_PORT}")

while True:
    # Receive data from the client
    data, addr = server_socket.recvfrom(1024)

    # Process the request (compute result of the function)
    result = time.time()  # Replace this with your actual function
    result = math.sin(2 * math.pi * parameter)

    # Print server information
    print(f"Received request from {addr} at {time.time()}")
    print(f"Sending result {result} to {addr} at {time.time()}")

    # Send the result back to the client
    server_socket.sendto(str(result).encode(), addr)

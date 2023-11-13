import socket
import time

# Client settings
UDP_IP = "0.0.0.0"  # Replace with the actual IP of router00
UDP_PORT = 55055

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Send a request to the server
    client_socket.sendto(b"Request", (UDP_IP, UDP_PORT))

    # Receive the result from the server
    data, addr = client_socket.recvfrom(1024)
    result = float(data.decode())

    # Print the received result
    print(f"Received result {result} from {addr} at {time.time()}")

    # Sleep for some time before sending the next request
    time.sleep(1)

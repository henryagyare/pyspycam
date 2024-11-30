import socket
import cv2
import pickle
import struct

# Set up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Server IP
port = 9999
client_socket.connect((host, port))

data = b""  # Buffer to store data
payload_size = struct.calcsize("Q")  # Size of packed frame length

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(4 * 1024)  # Receive data in chunks
        if not packet:
            break
        data += packet

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(4 * 1024)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Deserialize frame and display
    frame = pickle.loads(frame_data)
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow('Client: Receiving Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

client_socket.close()
cv2.destroyAllWindows()

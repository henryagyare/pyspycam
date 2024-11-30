import socket
import cv2
import pickle
import struct

# Set up server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'  # Listen on all available interfaces
port = 9999
server_socket.bind((host, port))
server_socket.listen(5)
print("Server listening on port", port)

# Accept client connection
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")

# OpenCV video capture
capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # Encode frame as JPEG
    _, buffer = cv2.imencode('.jpg', frame)
    data = pickle.dumps(buffer)  # Serialize frame
    message = struct.pack("Q", len(data)) + data  # Prepend frame size

    # Send frame to client
    client_socket.sendall(message)

    # Display the server-side video feed
    cv2.imshow('Server: Capturing Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
capture.release()
client_socket.close()
server_socket.close()
cv2.destroyAllWindows()

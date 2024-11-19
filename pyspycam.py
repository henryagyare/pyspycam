import cv2

# id of the video capturing device to open. To open default camera using default backend just pass 0.
capture = cv2.VideoCapture(0)

while True:
    _, frame = capture.read()
    #  We give the Window a name of "Capture from Webcam", and we also give it the frame which is an numpy object.
    # if frame.any():
    cv2.imshow("Capture from Webcam", frame)
    print(frame)
    # with open("pyspycamlog", "a") as spylogfile:
    #     frame_data = "".join(frame)
    #     spylogfile.write(frame_data)
    break
    # else:
    #     print("No frame")

    # We know that the ASCII code for the Escape key is 27.
    if cv2.waitKey(1) == 96:
        break

# Release the capture and destroy all OpenCV Windows.
capture.release()
cv2.destroyAllWindows()

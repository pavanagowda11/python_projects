import cv2

# Open camera
cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, frame = cap.read()

    if not ret:
        print("Cannot open camera")
        break

    # Flip camera horizontally
    flipped = cv2.flip(frame, 1)

    # Display flipped camera
    cv2.imshow("Flipped Camera", flipped)

    # Press Q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera
cap.release()
cv2.destroyAllWindows()
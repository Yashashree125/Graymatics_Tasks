import cv2

cap = cv2.VideoCapture('D:/Graymatics/TF/tensorflow/tensorflow/examples/label_image/videos/blockchain.mp4')

start_time = 30
end_time = 35

fps = cap.get(cv2.CAP_PROP_FPS)

start_frame = int(start_time * fps)
end_frame = int(end_time * fps)

#print(start_frame , end_frame)

cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

for i in range(start_frame, end_frame):
    ret, frame = cap.read()

    # For red rectangle 
    height, width, _ = frame.shape
    x = int((width - 100) / 2)
    y = int((height - 100) / 2)
    cv2.rectangle(frame, (x, y), (x+100, y+100), (0, 0, 255), 2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

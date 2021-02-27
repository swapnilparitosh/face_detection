from cv2 import cv2

#training data set
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture video
webcam = cv2.VideoCapture(0)

# looping over each frames caught by webcam
while True:
    # trueor false (boolean) in successful_frame_read and image in frame 
    successful_frame_read, frame = webcam.read()
    # convert into gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # detect face
    face_coordinates = trained_face_data.detectMultiScale(gray)
    print(face_coordinates)

    #draw rectangle aroung face
    for(x,y,w,h) in face_coordinates:
        cv2.rectangle(frame,(x,y),(x+w, y+h), (0,200,0),5)

    # show    
    cv2.imshow("Face Detection App",frame)
#     cv2.waitKey(1)
    key = cv2.waitKey(1)

    if key == 81 or key == 113:
        break
webcam.release()

print('code completed')
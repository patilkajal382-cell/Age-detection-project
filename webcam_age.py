import cv2
import numpy as np
import time
from tensorflow.keras.models import load_model

# load model once
model = load_model("age_model.h5")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


# function to start webcam and predict age
def predict_age_from_webcam():

    cap = cv2.VideoCapture(0)

    start_time = time.time()
    predictions = []

    while True:

        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:

            face = frame[y:y+h, x:x+w]

            face = cv2.resize(face,(200,200))
            face = face/255.0
            face = np.reshape(face,(1,200,200,3))

            prediction = model.predict(face)

            age = int(max(0,min(100,prediction[0][0])))

            predictions.append(age)

            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.putText(frame,"Scanning...",
                        (x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0,255,0),
                        2)

        cv2.imshow("Age Detection",frame)

        if time.time() - start_time > 5:
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # calculate average
    if len(predictions) > 0:
        final_age = int(sum(predictions)/len(predictions))
    else:
        final_age = 0

    return final_age
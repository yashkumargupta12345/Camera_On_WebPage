import streamlit as st
import cv2
from datetime import datetime

st.title("Motion Detector")
start = st.button("Start Button")

if start :
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get Current Time as a Date Time Object
        now = datetime.now()

        # Get Day and Time Add to The Frame
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30,80),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3,
                    color=(255,255,255), thickness =2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=3,
                    color=(255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)



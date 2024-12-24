import streamlit as st
from PIL import Image

with st.expander("Start Camera"):
    #Start the camera
    camera_image = st.camera_input("my camera")
    
    #create pillow image instance
    if camera_image:
        img = Image.open(camera_image)
        #Convert the  grayscale image
        gray_img = img.convert("L")
        #show the image
        st.image(img)
    
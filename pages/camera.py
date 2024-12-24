import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image = st.file_uploader("Upload Image")

with st.expander("Start Camera"):
    #Start the camera
    camera_image = st.camera_input("my camera")

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    gray_imgage = image.convert("L")
    st.image(gray_imgage)


    
#create pillow image instance
if camera_image:
    img = Image.open(camera_image)
    #Convert the  grayscale image
    gray_img = img.convert("L")
    #show the image
    st.image(gray_img)
    
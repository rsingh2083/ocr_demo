# Instructions on How to use OCR on Hikey960

OCR demo application allows user to recognize English characters in a image/video by selecting a particular region of that interest.

Hardware required: Hikey 960, USB Video Camera, PC

# Pre-requisites for Hikey960:

sudo apt-get update 

sudo apt install python3-dev python3-pip tesseract-ocr

pip3 install pytesseract 

OpenCV on python3

Perform the following steps for the OCR Demo:

# Step 0:
Clone this repository using git clone
$ git clone 

# Step 1:

Run the test_roi.py

python3 test_roi.py

# Step 2:

Press 's' and this will open a Roi selector window. Click, press and drag to select a region in which you want to detect text. 

Note : The text in the selected region should be clear and the background noise in the image should be less to get more accuracy.

# Step 3:

You can retry the process by pressing 's' or quit by pressing 'q' on the window

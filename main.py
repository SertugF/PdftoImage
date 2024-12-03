# activate env pdf2im, needs python 3.7+
# conda create --name myenv python=3.7
# activate env
# pip install pdf2image
# create two directories Data_In, Data_Out
# put pdf into Data_In, get jpg for all pages from data_out
# higher dpi values incrase size drastically


# get file
from pdf2image import convert_from_path
import os

dataInPath = os.path.join("Data_In", "exdata.pdf")  # change pdf Name
pages = convert_from_path(dataInPath, 200)  # dpi 200

os.chdir("Data_Out")

# save file
for count, page in enumerate(pages):
    page.save(f"out{count}.jpg", "JPEG")

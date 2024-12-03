# activate env pdf2im, needs python 3.7+
# conda create --name myenv python=3.7
# activate env
# pip install pdf2image


# get file
from pdf2image import convert_from_path

pages = convert_from_path("pdf_file", 500)

# save file
for count, page in enumerate(pages):
    page.save(f"out{count}.jpg", "JPEG")

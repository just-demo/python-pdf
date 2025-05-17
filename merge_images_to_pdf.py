from fpdf import FPDF
from PIL import Image

images = [
    'data/image/in-1.png',
    'data/image/in-2.png',
]

pdf = FPDF()

for image in images:
    pdf.add_page()
    img = Image.open(image)
    width, height = img.size
    pdf.image(image, 5, 5, 200, 200 * height / width)

pdf.output("data/image/out.pdf")

print('OK')

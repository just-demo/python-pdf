from pypdf import PdfWriter

pdfs = [
    'data/pdf/in-1.pdf',
    'data/pdf/in-2.pdf',
]

writer = PdfWriter()

for pdf in pdfs:
    writer.append(pdf)

writer.write('data/pdf/out.pdf')
writer.close()

print('OK')

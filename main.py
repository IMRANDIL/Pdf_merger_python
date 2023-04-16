import PyPDF2

merger = PyPDF2.PdfMerger()

pdfFiles = ['1.pdf', '2.pdf', '3.pdf']

for file in pdfFiles:
    pdfFile = open(file,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)

pdfFile.close()

merger.write('merged.pdf')

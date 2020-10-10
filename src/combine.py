import glob
from PyPDF2 import PdfFileMerger, PdfFileReader

path = ""
allPdfFiles = glob.glob(path + "*.pdf")
merger = PdfFileMerger(strict=False)

for pdf in allPdfFiles:
    merger.append(PdfFileReader(pdf, strict=False))

merger.write(path + "merged.pdf")
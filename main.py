from PyPDF2 import PdfWriter, PdfReader

merger = PdfWriter()

# Take input from user about how many PDFs to merge
n = int(input("How many PDFs do you want to merge? "))

pdfs = []
for i in range(n):
    name = input(f"Enter the name of PDF file #{i+1} (with .pdf extension): ")
    pdfs.append(name)

# Open each PDF and add its pages to the merger
for pdf_file in pdfs:
    pdf_reader = PdfReader(pdf_file)  # Open the PDF file
    # Add each page from the PDF to the merger
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        merger.add_page(page)

# Create the final merged PDF file
output_filename = "merged-pdf.pdf"
with open(output_filename, "wb") as output_file:
    merger.write(output_file)

merger.close()

print(f"All PDFs merged successfully into {output_filename}")
# PDF Merger

This is a simple command-line PDF Merger tool written in Python using the PyPDF2 library.  
It allows you to combine multiple PDF files into a single PDF file with ease.

## Features

- Merge any number of PDF files
- User-friendly prompts for selecting files
- Saves the merged result as merged-pdf.pdf

## Requirements

- Python 3.x
- PyPDF2 library

Install PyPDF2 with the following command:

pip install PyPDF2
## How to Use
1. Clone or download this repository on your system.
2. Put all the PDF files you want to merge in the same folder as the script.
3. Run the script by executing:
4. Enter the number of PDF files to merge when prompted.
5. Enter each PDF file name (with .pdf extension) when asked.
6. The merged PDF named merged-pdf.pdf will be saved in the same folder.

## Example
How many PDFs do you want to merge? 3
Enter the name of PDF file #1 (with .pdf extension): file1.pdf
Enter the name of PDF file #2 (with .pdf extension): file2.pdf
Enter the name of PDF file #3 (with .pdf extension): file3.pdf
All PDFs merged successfully into merged-pdf.pdf
## Code Overview

The script works by:
- Taking the number of PDF files to merge as input.
- Accepting file names from the user.
- Opening each PDF with PyPDF2 and adding their pages to a PdfWriter object.
- Writing all content to a new merged PDF file.

## License
This project is free to use for learning and personal purposes.

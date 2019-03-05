from PyPDF2 import PdfFileMerger
import argparse
import sys

if __name__ == '__main__':
    # Command-line arguments
    parser = argparse.ArgumentParser(description="Unite many PDF files into a single one.")
    parser.add_argument('pdffiles', nargs='+', metavar='PDFFILE', help='Files to unite. They will be appended in the order passed.')
    parser.add_argument('-o', '--output', type=argparse.FileType('wb'), default="out.pdf", help='Output file. If not specified, a file called "out.pdf" will be used.')
    
    args = parser.parse_args()

    # Main logic
    pdfMerger = PdfFileMerger()

    for pdfFile in args.pdffiles:
        pdfMerger.append(pdfFile)
    
    pdfMerger.write(args.output)

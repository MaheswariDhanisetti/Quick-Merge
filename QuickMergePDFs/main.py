import PyPDF2
import tkinter as tk
from tkinter import filedialog

# Function to select PDF files
def select_files():
    # Create a new instance of the Tkinter root window
    root = tk.Tk()
    # Hide the root window since we only need the file dialog
    root.withdraw()
    # Open a file dialog to allow the user to select multiple PDF files
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files to merge",  # Set the title of the file dialog window
        filetypes=[("PDF files", "*.pdf")],  # Limit the selection to PDF files only
        multiple=True  # Allow multiple files to be selected
    )
    # Convert the selected file paths from a tuple to a list
    return root.tk.splitlist(file_paths)

# Get the list of PDF files from the user
pdfFiles = select_files()

# Create a PdfMerger object to manage the merging process
merger = PyPDF2.PdfMerger()

# Iterate through the list of PDF files
for filename in pdfFiles:
    # Open each PDF file in read-binary mode
    pdfFile = open(filename, 'rb')
    # Create a PdfReader object for the opened file
    pdfReader = PyPDF2.PdfReader(pdfFile)
    # Append the PdfReader object (representing the PDF file) to the merger
    merger.append(pdfReader)
    # Close the file (moved inside the loop to ensure each file is closed after being read)
    pdfFile.close()

# Write the merged PDF to a new file called 'merged.pdf'
merger.write('merged.pdf')

# Close the merger object (not strictly necessary but good practice)
merger.close()

print("PDF files have been successfully merged into 'merged.pdf'.")

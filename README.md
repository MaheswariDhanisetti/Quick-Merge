# PDF Merger

This project provides a simple script to merge multiple PDF files into a single PDF file using Python. The script utilizes the `PyPDF2` library for handling PDF files and `tkinter` for a graphical file selection dialog.

## Features

- Select multiple PDF files to merge using a graphical file dialog.
- Merge selected PDF files into a single PDF.
- Output the merged PDF as `merged.pdf`.

## Requirements

- Python 3.x
- `PyPDF2` library
- `tkinter` library (comes pre-installed with standard Python installations)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/pdf-merger.git
    cd pdf-merger
    ```

2. **Install required Python libraries**:
    ```bash
    pip install PyPDF2
    ```

## Usage

1. **Run the script**:
    ```bash
    python merge_pdfs.py
    ```

2. **Select PDF files**:
    - A file dialog will appear allowing you to select the PDF files you want to merge.
    - Select the files and click "Open".

3. **Merge the PDFs**:
    - The script will merge the selected PDF files into a single file named `merged.pdf` in the same directory.

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements
PyPDF2 - A library for working with PDF files in Python.
tkinter - The standard GUI toolkit for Python.

If you encounter any issues or have questions, please feel free to open an issue in this repository.

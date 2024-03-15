# PDF2Text-OCR-Toolkit

Welcome to the `PDF2Text-OCR-Toolkit` repository! This toolkit is designed to convert PDF files into editable text formats using Optical Character Recognition (OCR) technology. It streamlines the process of extracting text from scanned PDF documents and images, making it an invaluable tool for data processing, digital archiving, and content management.

## Features

- **PDF to Image Conversion:** Converts each page of a PDF file into separate image files.
- **Image to Text Extraction:** Utilizes OCR to extract text from images.
- **Text Merging:** Merges all extracted text files into a single comprehensive document.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.x
- [Pillow (PIL Fork)](https://python-pillow.org/)
- [PyTesseract](https://github.com/madmaze/pytesseract)
- [pdf2image](https://github.com/Belval/pdf2image)

Additionally, you'll need to install [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract). Please follow the installation instructions on their GitHub page, and remember to set the path to `tesseract.exe` in your script accordingly if you're using Windows.

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/yourusername/PDF2Text-OCR-Toolkit.git
cd PDF2Text-OCR-Toolkit
```

Install the required Python packages:

```
pip install -r requirements.txt
```

## Usage

1. **Prepare Your PDF File:** Place the PDF file you wish to convert in the `./data/pdfs` directory and rename it to `example_pdf.pdf` or update the `pdf_name` variable in the script accordingly.
2. **Run the Toolkit:** Execute the main script to start the conversion process.

```bash
python main.py
```

3. **Choose an Action:** The script will prompt you to choose one of the following actions:
   - `1` for PDF to Images Conversion
   - `2` for Images to Text Conversion
   - `3` for Merging Text Files

Type your choice and press `Enter` to proceed.

## Customization

You can customize the input and output paths, and other configurations by editing the variables at the top of the script.

## Contributing

Contributions to the `PDF2Text-OCR-Toolkit` are welcome! Feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
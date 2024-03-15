from pdf2image import convert_from_path
import os
import pytesseract
from PIL import Image

# Define the base directory for easier path management
base_dir = './data/'
pdf_name = 'example_pdf'

# Define paths
paths = {
    'images': os.path.join(base_dir, 'images', pdf_name),
    'text': os.path.join(base_dir, 'text', pdf_name),
    'merged': os.path.join(base_dir, 'merged', pdf_name)
}

# Create directories if they don't exist
for path in paths.values():
    os.makedirs(path, exist_ok=True)
    print(f"Folder {path} prepared!")

def pdf_to_image():
    print("PDF To Images Conversion Started")
    images = convert_from_path(os.path.join(base_dir, 'pdfs', pdf_name + '.pdf'))

    for i, image in enumerate(images):
        image_path = os.path.join(paths['images'], f'{pdf_name}_page_{i+1}.jpg')
        image.save(image_path, 'JPEG')
    print("PDF to Image Conversion Completed")

def multiple_images_to_multiple_text():
    print("Images To Text Conversion Started")
    # Note: Update the Tesseract path according to your installation
    pytesseract.pytesseract.tesseract_cmd = r'path_to_tesseract.exe'

    for filename in os.listdir(paths['images']):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(paths['images'], filename)
            image = Image.open(image_path)
            config = r'--psm 6'  # Adjust as needed
            text = pytesseract.image_to_string(image, config=config)
            text_path = os.path.join(paths['text'], os.path.splitext(filename)[0] + '.txt')

            with open(text_path, 'w', encoding='utf-8') as text_file:
                text_file.write(text)

    print("Images to Text Conversion Completed")

def merge_text_files():
    print("Merging Text Files Started")
    output_file_path = os.path.join(paths['merged'], 'merged_output.txt')
    
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for txt_file in os.listdir(paths['text']):
            if txt_file.endswith(".txt"):
                txt_filepath = os.path.join(paths['text'], txt_file)
                output_file.write(f"=== {txt_file} ===\n")

                with open(txt_filepath, 'r', encoding='utf-8') as txt_file_content:
                    output_file.write(txt_file_content.read() + '\n\n')

    print("Merging Text Files Completed")

def main():
    print("Choose an action:\n1. Convert PDF to Images\n2. Convert Images to Text\n3. Merge Text Files")
    user_choice = input("Enter your choice (1, 2, or 3): ")

    if user_choice == "1":
        pdf_to_image()
    elif user_choice == "2":
        multiple_images_to_multiple_text()
    elif user_choice == "3":
        merge_text_files()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()

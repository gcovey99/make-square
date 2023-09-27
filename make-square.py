from PIL import Image
import tkinter as tk
from tkinter import filedialog
import os 

def Reformat_Image_With_Ratio(desired_aspect_ratio):
    
    # Create a GUI window to prompt for file
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Show the file dialog and store the selected file path
    ImageFilePath = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])

    # If no file is selected, exit the function
    if not ImageFilePath:
        return

    # Extract the original file's name without its extension
    base_name = os.path.basename(ImageFilePath)
    file_name_without_extension, file_extension = os.path.splitext(base_name)

    # Create the new file name by appending "resize" to the original name
    output_file_name = file_name_without_extension + "-resize" + file_extension

    image = Image.open(ImageFilePath)
    width, height = image.size
    img_aspect_ratio = width/height
    
    if img_aspect_ratio != desired_aspect_ratio:
        if img_aspect_ratio > desired_aspect_ratio:
            # image is wider than desired aspect ratio
            new_width = width
            new_height = int(width / desired_aspect_ratio)
        else:
            # image is taller than desired aspect ratio
            new_height = height
            new_width = int(height * desired_aspect_ratio)

        # create a new blank image with the desired aspect ratio
        background = Image.new('RGBA', (new_width, new_height), (255, 255, 255, 0))  # make transparent background
        offset = (int((new_width - width) / 2), int((new_height - height) / 2))

        # paste the original image onto the blank image
        background.paste(image, offset)
        background.save(output_file_name, "PNG")  # Save with new file name in PNG format
        print(f"Image has been resized and saved as {output_file_name}")

    else:
        print("Image is already a valid aspect ratio, it has not been resized!")

Reformat_Image_With_Ratio(1/1)

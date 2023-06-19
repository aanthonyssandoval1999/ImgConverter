import sys
import os
from PIL import Image

image_folder = sys.argv[1] # Create a image folder to input the image to convert.
output_folder = sys.argv[2] # This is where the converted image will be stored.

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = img.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{filename}.png', 'png')
    print('all done!')

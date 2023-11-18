import sys
import os
from PIL import Image, ImageFilter

print("++++++++++++++++++++++")
print("+ Hellooo & Welcome! +")
print("++++++++++++++++++++++")
print("This is a JPG to PNG Converter!")

# tty: NO user input like standard
user_image = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Your folder {output_folder} was created!")

for filename in os.listdir(user_image):
    img = Image.open(f'{user_image}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done. Cheers!')


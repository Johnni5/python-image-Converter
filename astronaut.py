# ./image_data/astro.jpg

from PIL import Image, ImageFilter

img = Image.open('./image-data/astro.jpg')
print(img.size)
# thumbnail is inline !
img.thumbnail((400, 400)) #> do NOT use resize - thumbnail
img.save('astro-thumb.jpg')
print(img.size)

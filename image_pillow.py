from PIL import Image, ImageFilter

img = Image.open('./image-data/pikachu.jpg')

print(img)
print(img.info)
print(img.format)
print(img.mode)
print(img.size)
print(img.show())


filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur.png", 'png')


filtered_img_grey = img.convert('L')
filtered_img_grey.save("grey.png", 'png')

img = Image.open('./image-data/astro.jpg')
filtered_img = img.convert('L')
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey.png", 'png')

from PIL import Image, ImageFilter

before = Image.open("capt.bmp")
after = before.filter(ImageFilter.BoxBlur(1))
after.save("out.bmp")
from PIL import image, ImageDraw
from random import randit

def stega_encrypt():
	text = input("Введите текст: ")
	keys = []
	img = Image.open(input("Название картинки: "))
	draw = ImageDraw.Draw(img)
	width = img.size[0]
	height = img.size[1]
	pex = img.load()
	f = open('keys.txt', 'w')

	for elem in ([ord(elem) for elem in text]):
		key = (randit(1, width-10),randit(1,height-10))
		r,g,b = pix[key][:3]
		draw.point(key, (r,elem,b))
		f.write(str(key) + '\n')

	img.save("newimage.png", "PNG")
    f.close()

stega_encrypt()		
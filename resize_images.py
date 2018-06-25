import PIL
from PIL import Image  
from PIL import ImageDraw  
from PIL import ImageFont  
  
# Import operating system lib  
import os  


input_directory = '/Users/mak/Documents/Programming/Data/Images/'  
out_directory = '/Users/mak/Documents/Programming/Data/normal_Image/'    


for folder in os.listdir(input_directory):
	print(folder)
	if (folder[0] == '.'):
		continue
	if not os.path.exists(out_directory+folder):
		os.makedirs(out_directory+folder)
	for name in os.listdir(input_directory + folder + '/'):
		if (name[0] == '.'):
			continue
		filename = input_directory + folder + '/' + name
		filename_to = out_directory + folder + '/' + name
		im = Image.open(filename)
		# print(filename)
		rgb_im = im.convert('RGB')
		width, height = im.size
		up, down, left, right = height, 0, width, 0
		for h in range(height):
			for w in range(width):
				r, g, b = rgb_im.getpixel((w, h))
				if r > 40:
					if up > h:
						up = h
					if h > down:
						down = h
					if left > w:
						left = w
					if w > right:
						right = w
	
		size = max(down - up, right - left) + 3
		char_image = Image.new('L', (size, size), 0)  
		width, height = char_image.size
		k = left
		l = up
		for j in range((size - (right - left))/2, (size - (right - left))/2 + right - left + 1):
			for i in range((size - (down - up))/2, (size - (down - up))/2 + down - up + 1):
				char_image.putpixel((j,i), im.getpixel((k, l)))
				l += 1
			k += 1
			l = up

		char_image = char_image.resize((32, 32), Image.ANTIALIAS)

		char_image.save(filename_to)


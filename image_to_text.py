import pytesseract
from PIL import Image
import sys

output_file = 'output.txt'

def get_pixel(image,i,j):
	pixel_output = image.getpixel((i, j))
	if len(pixel_output) == 3:
		return pixel_output
	elif len(pixel_output) == 4:
		return pixel_output[1:]
	else:
		print("Pixel output = ", pixel_output, "\n")
		return pixel_output

def get_inverted_image_name(image_name):
	file_name = image_name.split(".")
	suffix = "_inverted"
	file_name_length = len(file_name)
	if file_name_length == 1:
		file_name[0] += suffix
	elif file_name_length > 1:
		file_name[file_name_length - 2] += suffix
	else:
		print("File name is ", file_name, " and it's filename length is ", file_name_length)

	joined_name = '.'.join(file_name)
	return joined_name
	
def invert_image_colours(image_name):
	image = Image.open(image_name)
	width, height = image.size
    
	for i in range(width):
		for j in range(height):
			r, g, b = get_pixel(image, i, j)
            
            # Invert the colors
			inverted_r = 255 - r
			inverted_g = 255 - g
			inverted_b = 255 - b
            
            # Set the inverted colors for the pixel
			image.putpixel((i, j), (inverted_r, inverted_g, inverted_b))
    
    # Save the modified image
	inverted_image_name = get_inverted_image_name(image_name)
	newImage = image.save(inverted_image_name)
    
	print("Image colours inverted. Inverted image saved as:", inverted_image_name)

def majorityCheck(image_name):
	image = Image.open(image_name)
	width, height = image.size
    
	white_pixels = 0
	black_pixels = 0
	
	for i in range(width):
		for j in range(height):
			r, g, b = get_pixel(image, i, j)
			brightness = (r + g + b) // 3
			
			if brightness > 127:
				white_pixels += 1
			else:
				black_pixels += 1

	if white_pixels > black_pixels:
		return 0
	else:
		return 1

def extract_text_from_image(image_name):
	text = pytesseract.image_to_string(image_name)
	f = open(output_file, 'w')
	f.writelines(text)
	f.close()
	print("Written data to ", output_file)
	
#Execution starts here
image_name = ""
command_line_input = sys.argv
if len(command_line_input) <= 1 :
	print("Give a valid image name (with file extension)")
	exit()
else :
	image_name = command_line_input[1]
	print("Image name = ", image_name)
	
if majorityCheck(image_name):
	invert_image_colours(image_name)
	extract_text_from_image(get_inverted_image_name(image_name))
else:
	extract_text_from_image(image_name)

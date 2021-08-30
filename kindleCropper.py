####################################
#A script to convert png images to properly fit kindle's screen ratio by cropping
#put the script in the image directory and run
import os
from PIL import Image

#file no. start
counter = 1;

def CropOne(loc):
	# Opens a image in RGB mode
	im = Image.open(loc)
	
	# Size of the image in pixels (size of original image)
	# (This is not mandatory)
	width, height = im.size
	
	# Setting the points for cropped image
	increment = width*(1072/1448) - 50
	left = 0
	top = 0
	right = width
	bottom = width*(1072/1448)
	global counter
	while bottom < height+increment:
		temp = im.crop((left, top, right, bottom))
		temp.save(str(counter) + ".png")
		counter = counter + 1
		top = top + increment
		bottom = bottom + increment

#get file directory names
path=os.getcwd()
dirListing = os.listdir(path)
editFiles = []
for item in dirListing:
	if ".png" in item:
		editFiles.append(path+'/'+item)

for filename in editFiles:
	CropOne(filename)
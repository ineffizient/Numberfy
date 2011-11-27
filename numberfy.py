#! /usr/bin/env python

from gimpfu import *
import glob
import random
 
def make_numbers(image, drawable, bg_color, size) : 
	# create image in the first place
	width = pdb.gimp_image_width(image)	
	height = pdb.gimp_image_height(image)
	new_image = gimp.Image(width, height, 0)

	# set background colour
	gimp.set_foreground(bg_color)
	background_layer = gimp.Layer(new_image, "background", width, height, 
		RGB_IMAGE, 100, NORMAL_MODE)
	new_image.add_layer(background_layer, 0 )	
        pdb.gimp_edit_bucket_fill(background_layer, 0, 0, 100, 0,0,0,0)
	
	# create number
	n_lines = height / size
 	x_position = 0
	for i in range (0,n_lines) : 
#		print "I am in line " + str(n_lines)
		while (x_position < width) : 
#			print "x_position is " + str(x_position)
			num = random.randint(0,9)
			extent = pdb.gimp_text_get_extents_fontname(str(num), size, 0, "Sans")
			if (extent[1] + x_position > width) : 
				break
			else:
				num_color = pdb.gimp_image_pick_color(image, drawable, x_position, i*size, 1, 1, size)
				gimp.set_foreground(num_color) 
		                pdb.gimp_text_fontname(new_image,background_layer , x_position, i*size, str(num), 0, 1, size, 0, "Sans") 
				x_position = x_position + extent[1]
		x_position = 0 
	
	pdb.gimp_selection_none(new_image)
	gimp.Display(new_image)
	return 


register(
       	"python_numberfy",
	"Numberfy Image",
	"Creates a copy of image with random numbers",
	"Avishek Sen Gupta",
	"Avishek Sen Gupta",
	"2011",
	"<Image>/Filters/Custom/Numberfy...",
	"*",
	[
		(PF_COLOR, 'background', 'The color of the background', (0,0,0)),
		(PF_INT, 'size', 'The size of a number in pixels.', 10), 

	],
	[],
	make_numbers,
        )

main()

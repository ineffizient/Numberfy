#! /usr/bin/env python

from gimpfu import *
import glob
import random
 
def make_numbers(image, drawable, width, height, special_number, bg_color, fg_color, hl_color, size) : 
	# create image in the first place
	
	new_image = gimp.Image(width, height, 0)

	# set background colour
	gimp.set_foreground(bg_color)
	background_layer = gimp.Layer(new_image, "background", width, height, 
		RGB_IMAGE, 100, NORMAL_MODE)
	new_image.add_layer(background_layer, 0 )	
        pdb.gimp_edit_bucket_fill(background_layer, 0, 0, 100, 0,0,0,0)
	
	# create number
	gimp.set_foreground(fg_color) 
	n_lines = height / size
 	x_position = 0
	magic_number = 0 
	current_line = ""
#	pdb.gimp_progress_init("Working...", '-1') 
	for i in range (0,n_lines) : 
#		print "I am in line " + str(n_lines)
		while (x_position < width) : 
#			print "x_position is " + str(x_position)
			num = random.randint(0,9)
			hl_flag = (num == magic_number) 
			extent = pdb.gimp_text_get_extents_fontname(str(num), size, 0, "Sans")
			if (extent[1] + x_position > width) : 
				break
			else: 
				if (hl_flag): 
				        gimp.set_foreground(hl_color)

#					hl_color = pdb.gimp_image_pick_color(image, drawable, x_position, i*size, 1, 1, size)
					if (magic_number == 9): 
						magic_number = 0
					else: 
						magic_number = magic_number + 1
				else: 
#                                        fg_color = pdb.gimp_image_pick_color(image, drawable, x_position, i*size, 1, 1, size)
					gimp.set_foreground(fg_color) 

		                pdb.gimp_text_fontname(new_image,background_layer , x_position, i*size, str(num), 0, 1, size, 0, "Sans") 
				x_position = x_position + extent[1]
		x_position = 0 
	
	# pdb.gimp_text_get_extents_fontname(text, size, size_type, fontname)
	pdb.gimp_selection_none(new_image)
	gimp.Display(new_image)
	return 


register(
       	"python_fu_make_numbers",
	"Fills random numbers",
	"Fills an image with random numbers",
	"Avishek Sen Gupta",
	"Avishek Sen Gupta",
	"2011",
	"<Image>/Filters/Custom/Make numbers...",
	"*",
	[
		(PF_INT, 'width', 'The width of the area to be filled', 1280), 
		(PF_INT, 'height', 'The height of the area to be filled', 1024),
		(PF_INT, 'special_number', 'The digit to be highlighted', 0),
		(PF_COLOR, 'background', 'The color of the background', (0,0,0)),
		(PF_COLOR, 'foreground', 'The color of the numbers.', (0,0,0) ), 
                (PF_COLOR, 'highlighted', 'The color of the highlighted numbers.', (0,0,0) ),
		(PF_INT, 'size', 'The size of a number in pixels.', 10), 

	],
	[],
	make_numbers,
        )

main()

# Maze solver using the Python Image Library (PIL)

A maze solver which uses the A* search algorithm to find the closest path. This code can be used by running the main.py file. It can be intertaining to draw mazes and watch this program solve them.

Maze requirements:
 - The maze must have a start and end.
 - The start must be colored in green, rgb code (0, 255, 0).
 - The end must be colored in red, rgb code (255, 0, 0).
 - The obsticles must be in black, rgb code (0, 0, 0).

A few things to look out for before running the code:
 - The maze's colors must be precice, since it is how the program detects the start, end and obsticles.
 - The time the program takes to solve mazes increases greatly as the image size increases. The recommended size would be 100x100 pixels.
 - Make sure to include the file type when writing the name of your file. for example .png or .jpg.
 - The solution will be saved in a file called solution.png.
 - Make sure to have your image in the same directory as the main.py and node.py files.

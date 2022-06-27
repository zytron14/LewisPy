#Import the libraries
from PIL import Image, ImageFont, ImageDraw
import math
import random

def draw_dot(draw, x, y, dot_size):
    draw.ellipse((x, y, x+dot_size, y+dot_size), fill='black', outline='black')
def draw_atom(draw, offset_x, offset_y, dot_size, abbr, num_valence):
    shifts = [(0, 0), (24, 0), (-12, 18), (-12, 50), (0, 68), (24, 68), (36, 18), (36, 50)]
    for shift in shifts:
        draw_dot(draw, offset_x+shift[0], offset_y+shift[1], dot_size)
    draw.text((offset_x, offset_y), abbr, font=myFont, fill=(0, 0, 0))
#Creating new Image object for background. The color 'scheme' is 'RGB' and the size IMG_WIDTH x IMG_HEIGHT pixels
myFont = ImageFont.truetype('font.otf', 64)
IMG_WIDTH = 800
IMG_HEIGHT = 800
img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), 'white') 

#Creating object from img to draw on.
draw = ImageDraw.Draw(img) 
#draw.ellipse((50, 50, 60, 100), fill='black', outline='black')
#draw.text((200, 200), "HEY GUYS", font=myFont, fill=(0, 0, 0))
#little demo for initial commit - looks acceptable
x = 0
y = 0
for letter in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]:
    draw_atom(draw, x, y, 8, letter, 8)
    x += 100
    if x >= IMG_WIDTH:
        x = 0
        y += 100

img.show()
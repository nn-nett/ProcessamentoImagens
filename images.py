from PIL import Image, ImageFilter
import os

os.getcwd()

img = Image.open('.\\Pokedex\\pikachu.jpg')

filtered_img = img.convert('L')
filtered_img.save("juju.png", 'png')


from PIL import Image, ImageFilter
from os import path

print(os.path.relpath)

img = Image.open('C:\\Users\\rpgni\\PycharmProjects\\ProcessamentoImagens\\venv\\Pokedex\\pikachu.jpg')

filtered_img = img.convert('L')
filtered_img.save("grey.png", 'png')


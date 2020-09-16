from PIL import Image, ImageFilter

img = Image.open('C:\\Users\\rpgni\\PycharmProjects\\ProcessamentoImagens\\venv\\Pokedex\\pikachu.jpg')
#filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img = img.convert('L')
filtered_img.save("grey.png", 'png')


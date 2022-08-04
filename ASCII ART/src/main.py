# = Libraries à Importer ===
import sys
import math
import pygame
from PIL import Image

# = Fonction Main ===
def main():
    print("Hello, There!")

    # = Variables ===
    running = True
    ascii_chars = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    colors_of_image = []
    text_of_image = ""

    # = Création de fenêtre
    pygame.init()
    display = pygame.display.set_mode((800, 800))

    # = Charger L'Image ===
    img = Image.open(sys.argv[1])
    pixel = img.load()

    for y in range(100):
        for x in range(100):
            colors_of_image.append(pixel[x, y])

            grey = math.floor(sum(pixel[x, y]) / 4)
            sys.stdout.write(ascii_chars[math.floor(grey * 71 / 255)])
            text_of_image += ascii_chars[math.floor(grey * 71 / 255)]

            if x % 100 == 0:
                sys.stdout.write("\n")

    # = Charger La Police d'écriture ===
    font  = pygame.font.Font("font/ARIALBD.TTF", 8)    
    font_idx, fonty, fontx = (0, 0, 0)

    # = Boucle Infinie ===
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if font_idx < len(text_of_image):
            text = font.render(text_of_image[font_idx], False, colors_of_image[font_idx])

            fontx += 1
            font_idx += 1
            if fontx % 100 == 0:
                fonty += 1
                fontx = 0
        
        display.blit(text, (fontx * 8, fonty * 8))
        pygame.display.flip()

    pygame.quit()

# = Appelle de la Fonction Main ===
if __name__ == "__main__":
    main()



import pygame
import os
import sys


# PYGAME
screen_width = 600
screen_height = 450
screen = pygame.display.set_mode((screen_width, screen_height))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


materics = ['africa.jpeg', 'america.jpeg', 'australia.jpeg']
run = True
count = 1
bg = pygame.image.load('img/africa.jpeg')
screen.blit(bg, (0, 0))
while run:
    if count == 3:
        count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            bg = pygame.image.load(f'img/{materics[count]}')
            count += 1
            screen.blit(bg, (0, 0))
    pygame.display.update()
pygame.quit()

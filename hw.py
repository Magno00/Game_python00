import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura = 640
altura = 400

tela = pygame.display.set_mode((640, 400))

pygame.display.set_caption("hello")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (0, 200, 0), (100, 150, 90, 50))
    pygame.display.update()


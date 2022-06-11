
from cmath import rect
import pygame

from pygame.locals import *

from sys import exit

pygame.init()

largura = 1000

altura = 680

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Churrasmon Alpha Deluxe Version 0.0.0.1')


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()       
            exit()
            
pygame.draw.rect(
    screen,
    [200, 200, 200],
    [100, 100, 30, 60],
        border_radius = 100
    )
pygame.draw.circle(tela, (0,0,255), (300,260), 40)
pygame.draw.circle(tela, 250,250,250,250,250,250)

            
pygame.display.update()
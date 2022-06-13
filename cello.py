# Imports
import sys
import pygame

# Configuration
pygame.init()
fps = 250
fpsClock = pygame.time.Clock()
altura, largura = 640, 480
tela = pygame.display.set_mode((altura, largura), pygame.RESIZABLE)
pygame.display.set_caption('Churrasmon Alpha Deluxe Version 0.0.0.1')

x = largura/2
y = 0


# Game loop.
while  True:
    tela.fill((20, 20, 20))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    pygame.draw.rect(
    tela,
    [250, 0, 0],
    [x, y, 30, 60],
    )
    
    if y >= altura:
        y = 0
    y = y + 1

    pygame.display.flip()
    fpsClock.tick(fps)

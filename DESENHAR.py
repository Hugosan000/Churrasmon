# Imports
import sys
import pygame

# Configuration
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

# Game loop.
while  True:
    screen.fill((20, 20, 20))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    pygame.draw.rect(
    screen,
    [200, 200, 200],
    [100, 100, 30, 60],
        border_radius = 100
    )

    pygame.display.flip()
    fpsClock.tick(fps)
import pygame 
from config import *
from pygame.locals import *

pygame.init()

screen= pygame.display.set_mode((SCREEN_WITDH,SCREEN_HEIGHT))
pygame.display.set_caption("mi primer juego")
screen.fill(PURPLE)

bg= pygame.image.load("assets/bg.jpg")
bg=pygame.transform.scale(bg, (SCREEN_WITDH, SCREEN_HEIGHT))   
screen.blit(bg, (0,0))

while True:
    for event in pygame.event.get():
        if event.type== QUIT:
            pygame.quit()
    pygame.display.update()
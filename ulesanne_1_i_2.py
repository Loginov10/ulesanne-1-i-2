import pygame
import sys

hall=[199, 194, 189]
black=[0,0,0]
white=[255,255,255]
orange=[250, 134, 32]

pygame.init()
ekraan=pygame.display.set_mode((300,300))
pygame.display.set_caption("Lumemees")



def Lumemees(ekraan, x, y):
    while True:
        event=pygame.event.poll()
        pygame.draw.ellipse(ekraan, white,[35+x, 20, 50, 50])
        pygame.draw.ellipse(ekraan, white,[23+x, 20+y, 80, 80])
        pygame.draw.ellipse(ekraan, white,[0+x, 65+y, 150, 150])
        pygame.draw.ellipse(ekraan, black,[70, 35, 5, 5])
        pygame.draw.ellipse(ekraan, black,[90, 35, 5, 5])
        pygame.draw.polygon(ekraan, orange,[[80, 50], [90, 50], 
                     [90, 70]])
        if event.type==pygame.QUIT:
            break
        pygame.display.flip()


Lumemees(ekraan,25,40)

pygame.init()
ekraani=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("barmalei")
pilt=pygame.image.load("gnom.jpg")
ekraan.blit(pilt,(182,278))


def gnom(ekraani):
    event=pygame.event.poll()
    pygame.init()
    ekraani=pygame.display.set_mode((500,500))
    pygame.display.set_caption("barmalei")
    ekraani.fill(white)
    pilt=pygame.image.load("gnom.jpg")
    ekraani.blit(pilt,(200,200))
    
    while True:
        pygame.draw.polygon(ekraan, hall,[[250, 350], [150, 300], [200, 300]])   
        pygame.draw.polygon(ekraan, hall,[[50, 50], [50, 300], [300, 300], [300,50]])
        tekst="Tere, Artjom"
        font=pygame.font.SysFont("Verdana",30)
        pilt1=font.render(tekst,False,(0,0,0))
        ekraani.blit(pilt1,(90,150))
        if event.type==pygame.QUIT:
                break
        pygame.display.flip()

gnom(ekraani)
pygame.quit()
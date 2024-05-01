import pygame
import math
import time     #libreria per gestione del tempo

pygame.init()   #serve per poter utilizzare pygame


h = 500 #altezza finestra
b = 500 #larghezza(base) finestra 

area = pygame.display.set_mode((b, h))
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

r = 30 #raggio

vriga = h/2
origa = b/2

hgiro = vriga - 3*r #posizione centrale dell'orbita circolare

vel = 0.01

vriga1=vriga #conservo il valore iniziale di priga

count = 0
while count < 4:            #RICORDA CHE è DA RIVEDERE IL pygame.event.get() per quittare dalla window
    
    while vriga >= hgiro:
        pygame.draw.circle(area, blue, (origa, vriga), r/2)
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro)) #luogo, colore, posizione estremo1, posizione estremo2
        pygame.display.update()
        time.sleep(vel)
        area.fill(black)
        vriga = vriga - 1
        origa = b/2 - math.sqrt((vriga1-hgiro)**2-(vriga-hgiro)**2)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    origa1 = origa
    while vriga != vriga1:
        pygame.draw.circle(area, blue, (origa, vriga), r/2)
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro))
        pygame.display.update()
        time.sleep(vel)
        area.fill(black)
        vriga = vriga + 1
        origa = origa1 + (b/2 - math.sqrt((vriga1-hgiro)**2-(vriga-hgiro)**2) - origa1)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    while vriga >= hgiro:
        pygame.draw.circle(area, blue, (origa, vriga), r/2)
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro))
        pygame.display.update()
        time.sleep(vel)
        area.fill(black)
        vriga = vriga - 1
        origa = b/2 + math.sqrt((vriga1-hgiro)**2-(vriga-hgiro)**2)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    origa2=origa
    while vriga != vriga1:
        pygame.draw.circle(area, blue, (origa, vriga), r/2)
        pygame.draw.line(area, green, (origa, vriga), (b/2, hgiro))
        pygame.display.update()
        time.sleep(vel)
        area.fill(black)
        vriga = vriga + 1
        origa = origa2 + (b/2 + math.sqrt((vriga1-hgiro)**2-(vriga-hgiro)**2) - origa2)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
    count = count + 1
    print(count)


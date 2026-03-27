import pygame

pygame.init()

win=pygame.display.set_mode((600,600))
pygame.display.set_caption("Car Drifting")

x=40
y=50
h=30
w=20
speed=20

run=True

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False 

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x-=speed
    
    if keys[pygame.K_RIGHT]:
        x+=speed

    if keys[pygame.K_UP]:
        y-=speed

    if keys[pygame.K_DOWN]:
        y+=speed
         
    win.fill((0,0,0))
    car=pygame.draw.rect(win,(255,255,255),(x,y,w,h))
    b=pygame.draw.
    pygame.display.update()

pygame.quit()

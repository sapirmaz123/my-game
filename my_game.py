import pygame
import random

# screen size 
WINDOW_W = 800
WINDOW_H = 500
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My Game")

clock = pygame.time.Clock()



IMAGE= 'background.jpg'
img= pygame.image.load(IMAGE)

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))


screen.blit(img, (0,0))


y= 20
for j in range(4):
    x= 20
    for i in range(WINDOW_W):
        pygame.draw.circle(screen, random_color(), (x, y), 15)
        x += 50
    y += 50


x_step1= WINDOW_W/2-30
x_step2= WINDOW_W/2+30


play = True
while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                x_step1 = -50
            if event.key == pygame.K_RIGHT: 
                x_step1 += 50 

    pygame.draw.line(screen, (0,200,0), [x_step1, 400], [x_step2, 400], width=10)
    pygame.display.flip()
    clock.tick(40)


pygame.quit()
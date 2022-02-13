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


color_list2 = []
def colors():
  for j in range(4):
   color_list1 = [] 
   for i in range(16):
      color_list1.append(random_color())
   color_list2.append(color_list1)

        


IMAGE= 'background.jpg'
img= pygame.image.load(IMAGE)

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))


x_start= WINDOW_W/2-30
x_end= WINDOW_W/2+30
circle_x= WINDOW_W/2
circle_y= 380

colors()

play = True

while play:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT: 
                x_start -= 50
                x_end -= 50
            if event.key == pygame.K_RIGHT: 
                x_start += 50
                x_end += 50 
    
    screen.blit(img, (0,0))
    y= 20
    for j in range(4):
        x= 20
        for i in range(16):
            pygame.draw.circle(screen, color_list2[j][i], (x, y), 15)
            x += 50
        y += 50
    pygame.draw.line(screen, (0,200,0), [x_start, 400], [x_end, 400], width=10)
    
    random_x= random.randint(0,800)
    random_y= random.randint(0,500)

    pygame.draw.circle(screen, (255,255,255), (circle_x, circle_y), 15)

    if circle_y >= 0 or circle_x <= 800 or circle_x >= 0:
        circle_x -= 10
        circle_y -= 40
        pygame.display.flip()
   
    if circle_y <= 0 or circle_x >= 800 or circle_x <= 0:
        circle_x += 10
        circle_y += 40
        pygame.display.flip()
          


    # pygame.display.flip()
    clock.tick(30)


pygame.quit()


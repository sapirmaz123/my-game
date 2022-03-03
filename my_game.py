from cgitb import text
from turtle import color
from typing import Counter
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
   

        
def is_ball_hit(x, y, circle_x, circle_y):
    return abs(x -circle_x) <50 and abs(y-circle_y) <50 

IMAGE= 'background.jpg'
img= pygame.image.load(IMAGE)
WINNER= 'winner.jpg'
win= pygame.image.load(WINNER)

def random_color():
    levels = range(32,256,32)
    return tuple(random.choice(levels) for _ in range(3))


x_start= WINDOW_W/2-30
x_end= WINDOW_W/2+30
circle_x= WINDOW_W/2
circle_y= 380

def is_line_hit(x_start, x_end, circle_x, circle_y):
    return abs(x_start -circle_x) <50 and abs(x_end -circle_x) <50 and abs(400-circle_y) <50 

def win(): 
   return color_list2.count('') == 64
        

colors()
end= True
play = True
up = True
counter= 0
hold= 0

while play:
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:         
            if event.key == pygame.K_LEFT: 
                hold = -1
            if event.key == pygame.K_RIGHT:
                hold = 1
        elif event.type == pygame.KEYUP:
            hold = 0
    x_start += 30*hold
    x_end += 30*hold
    screen.blit(img, (0,0))
    
    y= 20

    for j in range(4):
        x= 20
        for i in range(16):
            if color_list2[j][i] != '':
                pygame.draw.circle(screen, color_list2[j][i], (x, y), 15)
            if is_ball_hit(x, y, circle_x, circle_y):
                color_list2[j][i]= ''
                counter+=1 
            
            x += 50
        y += 50

    


    if x_start <=0:
        x_start= 0
        x_end= 50
    if x_start >= WINDOW_W:
        x_start= WINDOW_W
        x_end= WINDOW_W- 50
    pygame.draw.line(screen, (0,200,0), [x_start, 400], [x_end, 400], width=10)

    red = (150, 0, 0)
    font2 = pygame.font.SysFont(None, 90)
    text2 = font2.render('game over', True, red)

    random_x= random.randint(0,800)
    random_y= random.randint(0,500)

    color = (150, 40, 0)
    font1 = pygame.font.SysFont(None, 130)
    text1 = font1.render('win!', True, color)

    pygame.draw.circle(screen, (255,255,255), (circle_x, circle_y), 15)

    if is_line_hit(x_start, x_end, circle_x, circle_y):
        up = True

    if circle_y <= 0:
        up = False


    if win():
        print("win!!!")
        screen.blit(text1, (250, WINDOW_H/2-30))    

    elif circle_y >= WINDOW_H:
        screen.blit(text2, (250, WINDOW_H/2-30))    

    if circle_x >= WINDOW_W:
        end = True

    if circle_x <= 0:
        end = False

    if not end:
        circle_x += 10

    if end:
        circle_x -= 15

    if not up:
        circle_y += 30

    if up: 
        circle_y -= 40
    

     

    pygame.display.flip()
          


    clock.tick(15)


pygame.quit()





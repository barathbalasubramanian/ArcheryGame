
import pygame
import time
import random
pygame.init()
screen = pygame.display.set_mode((1200,800)) 
pygame.display.set_caption('ARCHERY')
arrow_img = pygame.image.load('archery1.png')
# width, height = arrow_img.get_width(), arrow_img.get_height()  # get size
picture = pygame.transform.scale(arrow_img, (164 ,164))
aim_img = pygame.image.load('001-archery.png')
# width_aim, height_aim = aim_img.get_width(), arrow_img.get_height()  # get size
picture_aim = pygame.transform.scale(aim_img, (164 ,164))
font = pygame.font.Font("freesansbold.ttf",32)
font1 = pygame.font.Font("freesansbold.ttf",60)
def show(x,y) :
    show = font.render(" SCORE : " + str(value) , True , (255,0, 0))
    screen.blit(show,(x,y))
def lost (x,y) :
    loses = font1.render(" GAME OVER " , True , (255,0, 0))
    screen.blit(loses,(x,y))
value = 0
lose = 0
line_x1 = 0
line_y1 = 400
line_x2 = 200 
line_y2 = 400
arrow_x = 0
arrow_y = 318
aim_y_change = 0
option  = [2,-2] 
show_x = 10
show_y = 10
random_move = random.choice(option)
def arrow ( x,y) :
    screen.blit(picture ,(x,y))
aim_x = 1050
aim_y = 318
def aim (x,y) :
    screen.blit(picture_aim ,(x,y))
def call() :
    global line_x1 ,line_x2,line_y1,line_y2 ,state
    line_x1 = 0
    line_y1 = 400
    line_x2 = 200
    line_y2 = 400
    state = 'not ready'
state = 'not ready'
run = True
while run :
    screen.fill((0,150,150))
    aim( aim_x,aim_y)
    line = pygame.draw.line(screen, (0,0,0),(line_x1,line_y1),(line_x2,line_y2), 3)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
        if event.type == pygame.KEYDOWN :
            if event.key  == pygame.K_SPACE :
                state = 'ready'
    if state == 'ready' :
        line_x1 += 4
        line_x2 += 4
    if line_x1 > 1200 :
        call()
        lose += 1
    if line_x2 == aim_x+86 :
        if aim_y < 355 and aim_y > 285 :
            value += 9
        if (aim_y > 355 and aim_y < 370 ) or (aim_y > 260 and aim_y < 285 ):
            value += 4
        if 395 > aim_y and aim_y > 250 :
            value += 1
            time.sleep(1)
            call()
    aim_y +=random_move 
    if aim_y > 650 :
        random_move = -2
    if aim_y < 0 :
        random_move = 2
    if lose > 3 :
        lost(400,400)
        state = 'not ready'
    arrow( arrow_x,arrow_y )
    show(show_x,show_y)
    pygame.display.update()
    
    
 
    
#pong
#by EdssongeraT

import pygame
pygame.init()

White=(255,255,255)
screen = pygame.display.set_mode((800,600))
done = True
#Player 1 coordinates
XP1 = 50
YP1 = 250

#Player 2 coordinates
XP2 = 730
YP2 = 250

#Ball coordinates
XB = 390
YB = 290

myfont = pygame.font.SysFont("monospace", 20)
clock = pygame.time.Clock()
#Movimientos
Speed = 6
ballSpX = 3
ballSpY = 3
#Score
ScoreP1=0
ScoreP2=0
#Game loop
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    keys = pygame.key.get_pressed()  
    #paddle events
    if keys[pygame.K_w]:
        YP1 -= Speed

    if keys[pygame.K_s]:
        YP1 += Speed

    if keys[pygame.K_UP]:
        YP2-= Speed

    if keys[pygame.K_DOWN]:
        YP2 += Speed
    #Bounds validations   
    if YP1 >= 500:
        YP1 = 500
    if YP2 >= 500:
        YP2 = 500  
    if YP1 <= 0:
        YP1 = 0
    if YP2 <= 0:
        YP2 = 0     
    if YB >= 580 or YB<=0:
        ballSpY*=-1
    #Scores
    if XB <= 1:
        ScoreP2+=1
        XB=390
        YB=290
        ballSpX=-3
        ballSpY=-3
    if XB >= 749:
        ScoreP1+=1
        XB=390
        YB=290
        ballSpX=3
        ballSpY=-3
    #Ball movement
    XB -= ballSpX
    YB += ballSpY
    #paints screen black
    screen.fill((0,0,0))
    #Scores
    label = myfont.render("Pong!", 1, (255,255,255))
    label1 = myfont.render("Player 1= "+str(ScoreP1), 1, (255,255,255))
    label2 = myfont.render("Player 2= "+str(ScoreP2), 1, (255,255,255))
    screen.blit(label, (390, 0))
    screen.blit(label1, (0, 0))
    screen.blit(label2, (660, 0))
    #draw paddles
    Player1 = pygame.draw.rect(screen,White,(XP1,YP1,20,100))
    Player2 = pygame.draw.rect(screen,White,(XP2,YP2,20,100))
    #draw ball
    Ball = pygame.draw.rect(screen,White,(XB,YB,20,20))
    #Collision
    if Ball.colliderect(Player1) or Ball.colliderect(Player2):
        ballSpX*=-1
    #Win
    if ScoreP1==5:
        ScoreP1 = 0
        ScoreP2 = 0
    if ScoreP2==5:
        ScoreP1 = 0
        ScoreP2 = 0
    #screen repaint
    pygame.display.update()
    clock.tick(60)
    
pygame.quit()

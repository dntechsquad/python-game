import pygame
import random
from gameobject import player
from gameobject import Wall
from gameobject import invisiblewall
from gameobject import trickwall
from gameobject import diewall
from gameobject import victorywall

whiteScreen = True
running = True
fps=60
BLACK = (0,0,0)
WHITE = (255,255,255)
Brown = (152, 106, 82)
DIE = (152, 106, 81)
playerX=150
playerY=150

#start up Pygame
pygame.init()
#start up sound module for pygame
pygame.mixer.init()
# Set up the screen for
screen= pygame.display.set_mode((1280,720))
# Keeps track of game clock
clock = pygame.time.Clock()

#start timer
start_ticks=pygame.time.get_ticks()
timer = 0

#Create player
player = player(screen)
print(player.__class__.__name__)

#Create a list to hold all sprites
all_sprites = pygame.sprite.Group()
#Add sprites to our list of
all_sprites.add(player)

#container for Walls
#testlist = ["A","B","C"]



walls = pygame.sprite.Group()

#create a latout
layout = ["WWWWWWWWWWWTTTTTTTWWWWDDDDDDDDDDDDDDDDDDDDTTTTTTTTTTTTTTTDDDDDDDDDDDDDDDDDWWWWWWWWDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDWWDDDDDWWWWWWWWWWW",
          "W                                                                                                                                        W",
          "W                                                                                                                                        W",
          "W                                                             DDD                                                                        W",
          "W                                                            DV  D       IIII  IIIIIII                                                   W",
          "W                                                            DII D                                                                       W",
          "W          WWWWWW                               TTTTT        DI  D                                                                       W",
          "W                                                                                DDDD                                                    W",
          "W                                                                                                                                        W",
          "W                                                                                                                   I                    W",
          "W                          WWWDDDDWWW                                                        DDDDDDDDD              I                    W",
          "W                                                                                                                   I                    T",
          "W                                                    TTTDDDD                        I                               I                    T",
          "W                                                                                    I                                                   W",
          "W                                                                                     I                                                  W",
          "W                                                                                      I                                                 W",
          "W                                                                   WWW                                                                  T",
          "W                    TTTTTT                                   I                                                TTTTT                    IT",
          "W               I                                                                                                          I             T",
          "W               I                                                                                                         I              D",
          "W                I                      WWWWWW    WDW                                                                                    D",
          "W                I                                                                                   TTTTT                               W",
          "W                I                                                                                                                       V",
          "WWWWWWTTTTWWWWWWWWWWWW       WWWDDDDDWWWWWWWWW    WWW         TDWT   TTT       DDDD       WWWWW   IIIII        DDDDDDD                  VW"]

x=0
y=0
size=30

for row in layout:
    for col in row:
        if col == "W":
            walls.add( Wall((152, 106, 82),x,y,size) )
            x = x+size
        if col == "I":
            walls.add(invisiblewall((BLACK),x,y,size))
            x = x+size
        if col == "T":
            walls.add(trickwall((Brown),x,y,size))
            x = x+size
        if col == "D":
            walls.add(diewall((DIE),x,y,size))
            x = x+size
        if col == "V":
            walls.add(victorywall((WHITE),x,y,size))
            x = x+size
        if col == " ":
            x = x+size
    y = y+size
    x = 0

player.localWalls = walls
tricky = trickwall((WHITE),0,0,0)
#print(tricky.__class__.__name__)


#pygame.draw.rect(x,y,w,h)



while running :
    # Set the game speed
    clock.tick(fps)
    screen.fill(BLACK)
    #track time spent in game
    timer = (pygame.time.get_ticks() - start_ticks)/1000
    player.timer = timer

    #Change background
    #if  whiteScreen:
        #screen.fill(WHITE)
        #whiteScreen = False
    #else:
        #screen.fill(BLACK)
        #whiteScreen = True

    # Process Input
    for event in pygame.event.get():
        # Check for exiting out of window
        if event.type == pygame.QUIT :
            running = False

        #PROCESS control
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    #make the player go K_LEFT
                    player.goLeft()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                #stop moving K_LEFT
                player.stop()

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #make the player go K_RIGHT
                    player.goRight()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                #stop moving K_RIGHT
                player.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                #make the player go K_UP
                player.jump()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                #stop moving K_UP
                player.stop()




    # Process controls continuously
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_RIGHT]:
    #    playerX = playerX + 30
    #if keys[pygame.K_LEFT]:
    #    playerX = playerX - 30
    #if keys[pygame.K_UP]:
    #    playerY = playerY - 30
    #if keys[pygame.K_DOWN]:
    #    playerY = playerY + 30





    # Drawing our player
    #pygame.draw.rect(screen, (62,127,232) , (playerX,playerY, 100,100))


    all_sprites.update()
    all_sprites.draw(screen)

    # Drawing all walls
    walls.draw(screen)

    #Display new screen
    pygame.display.flip()
    # End of while loop

print(timer)

pygame.quit()

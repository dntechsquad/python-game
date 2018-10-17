import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
Brown = (152, 106, 82)
DIE = (152, 106, 81)

class player(pygame.sprite.Sprite):

#set movement
    change_x = 0
    change_y = 0


#starting
    start_x=100
    start_y=100
    timer = 0

#Positions od death
    die_x = 0

    localWalls = pygame.sprite.Group()

    def __init__(self,screen):
        #lets us use sprites
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((20,20))
        pygame.draw.rect(screen,(255,255,255),(150,150,100,100))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (100,100)

    def update(self):
        self.rect.x = self.rect.x + self.change_x

        #Determine the change along y
        self.calcGrav()

        self.rect.y = self.rect.y + self.change_y

        #Check platform colitistion
        for wall in self.localWalls:
            if self.rect.colliderect(wall.rect) and wall.__class__.__name__ != "trickwall":

                if wall.victory == 1:
                    print("You're a winner! Here's your time:")
                    print(player.timer) #make the timer into an object I can put in multiple places
                    print ("Try to do it faster this time!")
                    wall.reset()

                if wall.color == DIE:
                    self.rect.center = (self.start_x,self.start_y)
                    for wall in self.localWalls:
                        wall.reset()
                if self.change_y > 0 and self.rect.bottom < wall.rect.bottom:
                    self.rect.bottom = wall.rect.top
                    self.change_y = 0

                elif self.change_y < 0 and self.rect.top > wall.rect.top:
                    self.rect.top = wall.rect.bottom
                    self.change_y = 0

                elif self.rect.bottom > wall.rect.top and self.rect.x < wall.rect.x:
                    self.rect.right = wall.rect.left

                elif self.rect.bottom > wall.rect.top and self.rect.x > wall.rect.x:
                    self.rect.left = wall.rect.right

#check how far right player is in the Screen
        if self.rect.x > 500:
            for wall in self.localWalls:
                wall.rect.x -= self.change_x
                self.rect.x = 499

        if self.rect.y>720:
            #Save Position
            self.die_x = self.rect.x
            self.rect.center = (self.start_x , self.start_y)
            for wall in self.localWalls:
                wall.reset()



    def calcGrav(self):

        if self.change_y == 0:
            self.change_y = 1

        else :
            self.change_y = self.change_y + .5

    def goLeft(self):
        self.change_x = -5

    def goRight(self):
        self.change_x = 5

    def stop(self):
        self.change_x = 0

    def jump(self):
        #test if there's anything below us
        self.rect.y += 2
        wallHitlist = pygame.sprite.spritecollide(self, self.localWalls ,False)
        self.rect.y -= 2
        #if sth below , than jump
        if len(wallHitlist) > 0:
            self.change_y = -8

        #Does a double jump
        self.change_y = -8


class Wall(pygame.sprite.Sprite):

    #starting possition
    start_x = 0
    start_y = 0
    victory = 0
    def __init__(self,color,x,y,s):


        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((s,s))


        self.rect = pygame.Rect(x,y,s,s)
        # (x,y,width,heights)
        self.image.fill(color)

        self.start_x = x
        self.start_y = y
        self.color = color

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y



class invisiblewall(pygame.sprite.Sprite):

    #starting Positions
    start_x = 0
    start_y = 0
    victory = 0

    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)



        self.image = pygame.Surface((s,s))


        self.rect = pygame.Rect(x,y,s,s)
        # (x,y,width,heights)
        self.image.fill(BLACK)

        self.start_x = x
        self.start_y = y
        self.color = c

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y


class trickwall(pygame.sprite.Sprite):

    #starting Positions
    start_x = 0
    start_y = 0
    victory = 0

    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)



        self.image = pygame.Surface((s,s))


        self.rect = pygame.Rect(x,y,s,s)
        # (x,y,width,heights)
        self.image.fill(Brown)

        self.start_x = x
        self.start_y = y
        self.color = c

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y

class diewall(pygame.sprite.Sprite):

    #starting Positions
    start_x = 0
    start_y = 0
    victory = 0

    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)



        self.image = pygame.Surface((s,s))


        self.rect = pygame.Rect(x,y,s,s)
        # (x,y,width,heights)
        self.image.fill(DIE)

        self.start_x = x
        self.start_y = y
        self.color = c

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y

class victorywall(pygame.sprite.Sprite):

    #starting Positions
    start_x = 0
    start_y = 0
    victory = 1

    def __init__(self,c,x,y,s):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface((s,s))

        self.rect = pygame.Rect(x,y,s,s)
        # (x,y,width,heights)
        self.image.fill(WHITE)

        self.start_x = x
        self.start_y = y
        self.color = c

    def reset(self):
        self.rect.x = self.start_x
        self.rect.y = self.start_y

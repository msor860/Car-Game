import pygame,sys
from pygame.locals import *
import random
import time
pygame.init()
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
DARKGREEN = (0, 175, 0)
RED = ( 255, 0, 0)
BLUE = ( 0, 0, 255)
YELLOW = ( 0, 255, 255)
GRAY = (175,175,175)
SCREEN_WIDTH = 360
SCREEN_HEIGHT = 500
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCORE = 0
SPEED = 5
#screen = pygame.display.set_mode(size)
pygame.display.set_caption("The Vroom Vrooms")
# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True
lane_cor = [190, 320, 450, 580]
# The clock will be used to control how fast the screen updates
FramePerSec = pygame.time.Clock()
FPS = 60

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((size))
DISPLAYSURF.fill(WHITE)
# -------- Main Program Loop -----------

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("Player.png")
    self.surf = pygame.Surface((40, 75))
    #self.rect = self.surf.get_rect(center = (320, 450))
    self.rect = self.surf.get_rect(center = (160,460))
  def move(self):
    pressed_keys = pygame.key.get_pressed()
    if self.rect.left > 0:
      if pressed_keys[K_LEFT]:
        self.rect.move_ip(-5, 0)
    if self.rect.right < SCREEN_WIDTH:
      if pressed_keys[K_RIGHT]:
        self.rect.move_ip(5, 0)
  #def draw(self,surface):
    #surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super().__init__()
    self.image = pygame.image.load("Enemy.png")
    self.surf = pygame.Surface((42, 70))
    self.rect = self.surf.get_rect(center = (random.randint(40,SCREEN_WIDTH-40), 0))
  def move(self):
    global SCORE
    self.rect.move_ip(0, SPEED)
    if (self.rect.bottom > 600):
      SCORE += 1
      self.rect.top = 0
      self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


p1 = Player()
e1 = Enemy()

#Creating Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(e1)
all_sprites = pygame.sprite.Group()
all_sprites.add(p1)
all_sprites.add(e1)

#Adding a new User event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
  # --- Main event loop
  #Cycles through all events occuring
  for event in pygame.event.get(): # User did something
    if event.type == INC_SPEED:
      SPEED += 0.5
    if event.type == pygame.QUIT: # If user clicked close
      pygame.quit()
      sys.exit()
  
  DISPLAYSURF.blit(background, (0,0))
  scores = font_small.render(str(SCORE), True, BLACK)
  DISPLAYSURF.blit(scores, (10,10))
       # Flag that we are done so we exit this loop
  #p1.update()
  #p1.draw(DISPLAYSURF)
  #e1.update()
  #e1.draw(DISPLAYSURF)
  #pygame.display.update()
  #FramePerSec.tick(FPS)
  # --- Game logic should go here
  for entity in all_sprites:
    DISPLAYSURF.blit(entity.image,entity.rect)
    entity.move()

  #To be run if collision occurs between Player and Enemy
  if pygame.sprite.spritecollideany(p1, enemies):
    time.sleep(1)
    DISPLAYSURF.fill(RED)
    DISPLAYSURF.blit(game_over, (30,250))

    pygame.display.update()
    for entity in all_sprites:
      entity.kill()
    time.sleep(2)
    pygame.quit()
    sys.exit()
  # --- Drawing code should go here
  # First, clear the screen to white. 
 #### screen.fill(WHITE)
  #The you can draw different shapes and lines or add text to your background stage.
 # pygame.draw.rect(DISPLAYSURF, DARKGREEN, [0, 0, 125, 530],0)
 # pygame.draw.rect(DISPLAYSURF, GRAY, [126, 0, 125, 530],0)
 # pygame.draw.rect(DISPLAYSURF, GRAY, [252, 0, 125, 530],0)
 # pygame.draw.rect(DISPLAYSURF, GRAY, [378, 0, 125, 530],0)
 # pygame.draw.rect(DISPLAYSURF, GRAY, [504, 0, 125, 530],0)
 # pygame.draw.rect(DISPLAYSURF, DARKGREEN, [630, 0, 125, 530],0)
 # pygame.draw.rect(DISPLAYSURF, WHITE, [126, 0, 5, 530],0)
 # pygame.draw.rect(DISPLAYSURF, WHITE, [253, 0, 5, 530],0)
 # pygame.draw.rect(DISPLAYSURF, WHITE, [379, 0, 5, 530],0)
 # pygame.draw.rect(DISPLAYSURF, WHITE, [505, 0, 5, 530],0)
 # pygame.draw.rect(DISPLAYSURF, WHITE, [631, 0, 5, 530],0)
  

  


  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.update()
  FramePerSec.tick(FPS)
  
  # --- Limit to 60 frames per second
 
#Once we have exited the main program loop we can stop the game engine:

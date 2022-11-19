import pygame
import random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

#constants
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5,0)
            
        #keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,0))
        self.surf.fill((255,255,23))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.surf.right < 0:
            self.kill()


#initialize the game
pygame.init()

#setup the drawing window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#initialize the Player
player = Player()

#Create groups to hold all sprites
enemies = pygame.group.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True
#main loop
while running:
    
    for event in pygame.event.get():
        #Check for KEYDOWN
        if event.type == KEYDOWN:
            #Escape key
            if event.key == K_ESCAPE:
                running = False
        #Check for QUIT event
        elif event.type == QUIT:
            running = False
        
        # if event.type == pygame.QUIT:
        #     running = False
                
    #get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()                

    player.update(pressed_keys)

    #fill the screen with color (background)
    screen.fill(0x0c0515)
        
    #draw the player on the screen
    screen.blit(player.surf, player.rect)  
        
    #draw a solid blue circle in the center
    # pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    # circle =(window where to draw, RGB, ordered-pair location, radius)
        
    #update the display
    pygame.display.flip()

#quit pygame
pygame.quit()
# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from circleshape import *
from player import Player


updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
Player.containers = (updatable, drawable)

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH/2
    y = SCREEN_HEIGHT/2
    player = Player(x, y)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(BLACK)

        updatable.update(dt)
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
    
    

if __name__ == "__main__":
    main()
# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from circleshape import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = ((updatable))
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updatable:
            object.update(dt)

        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.kill()

        screen.fill(BLACK)
        
        for sprite in drawable:
            sprite.draw(screen)
        
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000
        
     

if __name__ == "__main__":
    main()
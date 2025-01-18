import pygame
import random
from constants import *
from circleshape import *

class Asteroid(CircleShape):
    containers = None

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.position , self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            a = self.velocity.rotate(random_angle)
            b = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_a.velocity = a * 1.2
            asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_b.velocity = b * 1.2
        
import pygame
import random

from constants import *
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        one = self.position.rotate(random_angle)
        two = self.position.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first = Asteroid(self.position.x, self.position.y, new_radius)
        second = Asteroid(self.position.x, self.position.y, new_radius)
        first.velocity = one * 1.2
        second.velocity = two * 1.2


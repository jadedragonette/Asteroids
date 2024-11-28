# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from a module
# into the current file
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()
    


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=000000, rect=None, special_flags=0)

        for update in updatable:
            update.update(dt)

        for roid in asteroids:
            if roid.collide(player):
                print("Game Over!")
                return
            for shot in shots:
                if roid.collide(shot):
                    shot.kill()
                    roid.split()

        for draw in drawable:
            draw.draw(screen)
        

        dt = clock.tick(60) / 1000
        pygame.display.flip()

    

if __name__ == "__main__":
    main()
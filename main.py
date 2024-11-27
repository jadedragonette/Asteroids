# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from a module
# into the current file
from constants import *

def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=000000, rect=None, special_flags=0)

    

if __name__ == "__main__":
    main()
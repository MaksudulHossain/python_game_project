import sys 
import pygame

class AlienInvasion:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Alien Invasion')

        #set bg 
        self.bg_color = (230,230,230)



    def run_game(self):

        while True:
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit() 

            # redraw 
            self.screen.fill(self.bg_color)

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
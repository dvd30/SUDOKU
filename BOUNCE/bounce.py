import pygame
import sys

pygame.init()
pygame.font.init()
height = width = 500
brick_color = (169, 64, 7)
cell_size = 50


class World:
    def __init__(self):
        self.world = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    def draw(self, screen):
        for row in self.world:
            for col in row:
                if self.world[row][col] == 1:
                    pygame.rect.draw(screen, brick_color, pygame.Rect(row*cell_size, col*cell_size,cell_size, cell_size))


def main():
    world = World()
    screen = pygame.display.set_mode((height, width))
    screen.fill((135, 206, 235))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        world.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()

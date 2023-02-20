import pygame, sys

from AI import AI
from player import Player
from const import *

from random import randint

pygame.init()

cell_colors = [(80, 80, 80), (100, 100, 100)]

delay = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

player = Player(screen, CELL_SIZE)

ai = AI(player.pos)

food = (randint(0, (WIDTH / CELL_SIZE) - 1), randint(0, (WIDTH / CELL_SIZE) - 1))

while food in player.pos:
    food = (randint(0, (WIDTH / CELL_SIZE) - 1), randint(0, (WIDTH / CELL_SIZE) - 1))

delay = 0

path = []

def get_path():
    ai.head = player.pos[0]
    ai.body = player.pos[1:]


    ai.algorithm(ai.grid, ai.head, food)
    path = ai.get_path()
    if len(path) != 0:
        path.pop()

    if len(path) != 0:
        path.insert(0, food)

    return path

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    if delay % 10 == 0:
        screen.fill('black')

        for a in range(int(WIDTH / CELL_SIZE)):
            for b in range(int(HEIGHT / CELL_SIZE)):
                pygame.draw.rect(screen, cell_colors[(a+b) % 2], (a * CELL_SIZE, b * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if path == []:
            path = get_path()


        fx, fy = food
        pygame.draw.rect(screen, (0, 0, 255), (fx * CELL_SIZE, fy * CELL_SIZE, CELL_SIZE, CELL_SIZE))

        if len(path) != 0:
            player.get_dir(path[-1])
        else:
            path = get_path()
            if len(path) != 0:
                player.get_dir(path[-1])

        
        player.move()

        # check if hit wall
        hx, hy = player.pos[0]
        if hx < 0 or hx > (WIDTH / CELL_SIZE) - 1 or hy < 0 or hy > (WIDTH / CELL_SIZE) - 1:
            pygame.quit()
            sys.exit()

        # check if player hit player body
        if (hx, hy) in player.pos[1:]:
            pygame.quit()
            sys.exit()

        # check if player ate food

        if player.add(food):
            food = (randint(0, (WIDTH / CELL_SIZE) - 1), randint(0, (WIDTH / CELL_SIZE) - 1))

            while food in player.pos:
                food = (randint(0, (WIDTH / CELL_SIZE) - 1), randint(0, (WIDTH / CELL_SIZE) - 1))

        player.draw()

        # delete last item of path

        if len(path) != 0:
            path.pop()


    delay += 1

    pygame.display.update()
    
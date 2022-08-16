# based on Eudreak! tutorial: https://www.edureka.co/blog/snake-game-with-pygame/

import pygame
import time
import random
from colorselection import ColorSelection

pygame.init()

display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('Snake by S. Dole')

snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font_style = pygame.font.SysFont("arial", 25)
score_font = pygame.font.SysFont("arial", 35)


def Your_score(score):
    value = score_font.render("Current Score: " + str(score), True, ColorSelection.yellow)
    display.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, ColorSelection.black, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_width / 6, display_height / 3])


def gameLoop():
    global snake_speed
    snake_speed = 15
    game_over = False
    game_close = False

    # player position
    x1 = display_width / 2
    y1 = display_height / 2

    # change in player movement
    x1_change = 0
    y1_change = 0

    snake_list = []
    Length_of_snake = 1

    # create food
    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    import colorselection

    while not game_over:

        while game_close:
            display.fill(ColorSelection.blue)
            message("Game over! Press Q to quit or C to continue!", ColorSelection.red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                    if event.type == pygame.QUIT:
                        game_over = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(ColorSelection.blue)
        pygame.draw.rect(display, ColorSelection.green, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > Length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            snake_speed += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()

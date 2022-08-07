import time
import pygame
import random

pygame.init()

sc_width = 600
sc_height = 400

screen = pygame.display.set_mode((sc_width, sc_height))
pygame.display.set_caption("Snake game by José de Brito")

white =  (255, 255, 255)
black = (0,0,0)
bg = (32, 42, 37)
red = (255,0,0)
yellow = (255, 255, 102)

game_over = False

block = 10


clock = pygame.time.Clock()
speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def score_snake(score, color):
    value = score_font.render("Your score: " + str(score), True, color)
    screen.blit(value, [0, 0])

def snake(s_block, s_list):
    for x in s_list:
        pygame.draw.rect(screen, white, [x[0], x[1], s_block, s_block])

def message(msg, color):
   message = font_style.render(msg, True, color)
   screen.blit(message, [sc_width/6, sc_height/3])

def looping_game():
    game_over = False
    game_close = False

    x = sc_width/2
    y = sc_height/2

    x_c = 0
    y_c = 0

    snake_list = []
    length_snake = 1

    foodx = round(random.randrange(0, sc_width - block)/10)*10
    foody = round(random.randrange(0, sc_width - block)/10)*10

    while not game_over:
        while game_close == True:
            screen.fill(white)
            message("You died, Press A to continue or Q to quit", red)
            score_snake(length_snake -1, red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        looping_game()
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_c = -block
                    y_c = 0
                elif event.key == pygame.K_RIGHT:
                  x_c = block
                  y_c = 0
                elif event.key == pygame.K_UP:
                     y_c = -block
                     x_c = 0
                elif event.key == pygame.K_DOWN:
                    y_c = block
                    x_c = 0

        if x >= sc_width or x < 0 or y >= sc_height or y < 0:
            game_close = True
        x = x + x_c
        y = y + y_c
        screen.fill(bg)
        pygame.draw.rect(screen, red, [foodx, foody, block, block])
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:
            del snake_list[0]
        
        for z in snake_list[:-1]:
            if z == snake_head:
                game_close = True

        snake(block, snake_list)
        score_snake(length_snake -1, yellow)


        pygame.display.update()
    
        if x == foodx and y == foody:
            foodx = round(random.randrange(0, sc_width - block) / 10.0) * 10.0
            foody = round(random.randrange(0, sc_height - block) / 10.0) * 10.0
            length_snake += 1

        clock.tick(speed)

    pygame.quit()
    quit()

looping_game()
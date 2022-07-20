import time
from threading import Thread
import random
import pygame as pg


pg.init()

win = pg.display.set_mode((541, 541))
win.fill((138, 43, 226))
body = pg.image.load('snake_body.png')
head = pg.image.load('snake_head.png')
black_square = pg.image.load('bl_sq.png')
gameover = pg.image.load('gameover.png')
gameover = pg.transform.scale(gameover, (401, 171))
food = pg.image.load('food.png')
board = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
         ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
run = True
game_over = False
snake = [[0, 0],
         [1, 0],
         [2, 0]
         ]
current_direction = 'right'


def place_food():
    global run
    count = 0

    while run:
        for i in range(1, 19):
            for j in range(1, 19):
                if board[i][j] == 3:
                    count = count + 1
        if count == 0:
            x = random.randrange(1, 19)
            y = random.randrange(1, 19)
            board[y][x] = 3
        count = 0
        time.sleep(0.003)


def place_snake():
    global run
    global board

    for cell in snake:
        snake_x = cell[0]
        snake_y = cell[1]
        board[snake_y][snake_x] = 1

    head_x = snake[-1][0]
    head_y = snake[-1][1]
    board[head_y][head_x] = 2


def click_buttons():
    global run
    global game_over
    global current_direction
    global event
    global board
    global snake
    if game_over is True:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if 374 <= event.pos[0] <= 417 and 281 <= event.pos[1] <= 305:
                    pg.quit()
                    exit(0)
                if 98 <= event.pos[0] <= 188 and 281 <= event.pos[1] <= 305:
                    game_over = False
                    win.fill((138, 43, 226))
                    board = [
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_'],
                        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                         '_']]
                    snake = [[0, 0],
                             [1, 0],
                             [2, 0]
                             ]

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_RIGHT and current_direction != 'left':
            current_direction = 'right'
        elif event.key == pg.K_LEFT and current_direction != 'right':
            current_direction = 'left'
        elif event.key == pg.K_UP and current_direction != 'down':
            current_direction = 'up'
        elif event.key == pg.K_DOWN and current_direction != 'up':
            current_direction = 'down'


def print_board():
    global win
    global black_square
    global board
    global snake
    global game_over
    for i in range(20):
        for j in range(20):
            if board[i][j] == 1 and [j, i] not in snake:
                board[i][j] = '_'
            if board[i][j] == '_':
                win.blit(black_square, (1 + j * (26 + 1), 1 + i * (26 + 1)))
            elif board[i][j] == 1:
                win.blit(body, (1 + j * (26 + 1), 1 + i * (26 + 1)))
            elif board[i][j] == 2:
                win.blit(head, (1 + j * (26 + 1), 1 + i * (26 + 1)))
            elif board[i][j] == 3:
                win.blit(food, (1 + j * (26 + 1), 1 + i * (26 + 1)))
            if game_over is True:
                win.blit(gameover, (70, 170))


def snake_movement():
    global current_direction
    global event
    global board
    global snake
    global game_over
    global run

    while run:
        if current_direction == 'right':
            x = snake[0][0]
            y = snake[0][1]
            board[y][x] = '_'
            snake = snake[1:]
            if snake[-1][0] == 19:
                snake.append([0, snake[-1][1]])
                snake = snake[1:]
            if board[snake[-1][1]][snake[-1][0] + 1] == '_':
                snake.append([snake[-1][0] + 1, snake[-1][1]])
            elif board[snake[-1][1]][snake[-1][0] + 1] == 3:
                snake.append([snake[-1][0] + 1, snake[-1][1]])
                snake.append([snake[-1][0] + 1, snake[-1][1]])
            elif board[snake[-1][1]][snake[-1][0] + 1] == 1:
                game_over = True


        elif current_direction == 'left':
            x = snake[0][0]
            y = snake[0][1]
            board[y][x] = '_'
            snake = snake[1:]
            if snake[-1][0] == 0:
                snake = snake[1:]
                snake.append([19, snake[-1][1]])
            if board[snake[-1][1]][snake[-1][0] - 1] == '_':
                snake.append([snake[-1][0] - 1, snake[-1][1]])
            elif board[snake[-1][1]][snake[-1][0] - 1] == 3:
                snake.append([snake[-1][0] - 1, snake[-1][1]])
                snake.append([snake[-1][0] - 1, snake[-1][1]])
            elif board[snake[-1][1]][snake[-1][0] - 1] == 1:
                game_over = True


        elif current_direction == 'up':
            x = snake[0][0]
            y = snake[0][1]
            board[y][x] = '_'
            snake = snake[1:]
            if snake[-1][1] == 0:
                snake = snake[1:]
                snake.append([snake[-1][0], 19])
            if board[snake[-1][1] - 1][snake[-1][0]] == '_':
                snake.append([snake[-1][0], snake[-1][1] - 1])
            elif board[snake[-1][1] - 1][snake[-1][0]] == 3:
                snake.append([snake[-1][0], snake[-1][1] - 1])
                snake.append([snake[-1][0], snake[-1][1] - 1])
            elif board[snake[-1][1] - 1][snake[-1][0]] == 1:
                game_over = True


        elif current_direction == 'down':
            x = snake[0][0]
            y = snake[0][1]
            board[y][x] = '_'
            snake = snake[1:]
            if snake[-1][1] == 19:
                snake = snake[1:]
                snake.append([snake[-1][0], 0])
            if board[snake[-1][1] + 1][snake[-1][0]] == '_':
                snake.append([snake[-1][0], snake[-1][1] + 1])
            elif board[snake[-1][1] + 1][snake[-1][0]] == 3:
                snake.append([snake[-1][0], snake[-1][1] + 1])
                snake.append([snake[-1][0], snake[-1][1] + 1])
            elif board[snake[-1][1] + 1][snake[-1][0]] == 1:
                game_over = True

        time.sleep(0.05)


thread1 = Thread(target=place_food, daemon=True)
thread2 = Thread(target=snake_movement, daemon=True)

thread1.start()
thread2.start()
print_board()

pg.display.update()
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

        if event.type == pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN:
            click_buttons()
    print_board()
    place_snake()
    pg.display.update()
    pg.time.delay(3)
pg.quit()

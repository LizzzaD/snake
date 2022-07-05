import time
from threading import Thread
import random
import pygame as pg

pg.init()

win = pg.display.set_mode((541, 541))
win.fill((138, 43, 226))
head = pg.image.load('snake_head.png')
body = pg.image.load('snake_body.png')
black_square = pg.image.load('bl_sq.png')
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
snake = [[2, 0],
         [1, 0],
         [0, 0]]


def print_food():
    global run

    while run:
        x = random.randrange(0, 20)
        y = random.randrange(0, 20)
        board[y][x] = 3
        time.sleep(3)





def print_snake():
    global run

    while run:
        for cell in snake:
            x = cell[0]
            y = cell[1]
            board[y][x] = 1







def click_buttons():
    global event
    global board
    global snake

    if event.key == pg.K_RIGHT and snake[0][0] == 19:
        x = snake[0][0]
        y = snake[0][1]
        board[y][x] = '_'
        snake = snake[1:]
        snake[-1][0] = 0
        if board[snake[-1][1]][snake[-1][0]+1] != 3:
            snake.append([0, snake[-1][1]])

        elif board[snake[-1][1]][snake[-1][0]+1] == 3:
            snake.append([0, snake[-1][1]])
            snake.append([1, snake[-1][1]])
        board[y][x] = 0

    if event.key == pg.K_RIGHT and board[snake[-1][1]][snake[-1][0]+1] != 1:
        x = snake[0][0]
        y = snake[0][1]
        board[y][x] = '_'
        snake = snake[1:]
        if board[snake[-1][1]][snake[-1][0]+1] != 3:
            snake.append([snake[-1][0]+1, snake[-1][1]])
        elif board[snake[-1][1]][snake[-1][0]+1] == 3:
            snake.append([snake[-1][0]+1, snake[-1][1]])
            snake.append([snake[-1][0]+1, snake[-1][1]])

    elif event.key == pg.K_LEFT and board[snake[-1][1]][snake[-1][0]-1] != 1:
        x = snake[0][0]
        y = snake[0][1]
        board[y][x] = '_'
        snake = snake[1:]
        if board[snake[-1][1]][snake[-1][0]-1] != 3:
            snake.append([snake[-1][0]-1, snake[-1][1]])
        elif board[snake[-1][1]][snake[-1][0]-1] == 3:
            snake.append([snake[-1][0]-1, snake[-1][1]])
            snake.append([snake[-1][0]-1, snake[-1][1]])

    elif event.key == pg.K_UP and board[snake[-1][1]-1][snake[-1][0]] != 1:
        x = snake[0][0]
        y = snake[0][1]
        board[y][x] = '_'
        snake = snake[1:]
        if board[snake[-1][1]-1][snake[-1][0]] != 3:
            snake.append([snake[-1][0], snake[-1][1]-1])
        elif board[snake[-1][1]-1][snake[-1][0]] == 3:
            snake.append([snake[-1][0], snake[-1][1]-1])
            snake.append([snake[-1][0], snake[-1][1]-1])

    elif event.key == pg.K_DOWN and board[snake[-1][1]+1][snake[-1][0]] != 1:
        x = snake[0][0]
        y = snake[0][1]
        board[y][x] = '_'
        snake = snake[1:]
        if board[snake[-1][1]+1][snake[-1][0]] != 3:
            snake.append([snake[-1][0], snake[-1][1]+1])
        elif board[snake[-1][1]+1][snake[-1][0]] == 3:
            snake.append([snake[-1][0], snake[-1][1]+1])
            snake.append([snake[-1][0], snake[-1][1]+1])




def print_board():
    global win
    global black_square
    global board
    for i in range(20):
        for j in range(20):
            if board[i][j] == '_':
                win.blit(black_square, (1 + j * (26 + 1), 1 + i * (26 + 1)))
            elif board[i][j] == 1:
                win.blit(body, (1 + j * (26 + 1), 1 + i * (26 + 1)))
            elif board[i][j] == 2:
                win.blit(head, (1 + j * (26 + 1), 1 + i * (26 + 1)))
            elif board[i][j] == 3:
                win.blit(food, (1 + j * (26 + 1), 1 + i * (26 + 1)))


thread1 = Thread(target=print_food, daemon=True)
thread2 = Thread(target=print_snake, daemon=True)

thread1.start()
thread2.start()
print_board()


pg.display.update()
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            thread1.join()
            thread2.join()

        if event.type == pg.KEYDOWN:
            click_buttons()

    print_board()
    pg.display.update()
    pg.time.delay(20)
pg.quit()
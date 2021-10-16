
import pygame, sys
import numpy as np

pygame.init()
WIDTH = 600
HEIGHT = 600
BOARD_ROWS = 3
BOARD_COL = 3
SQUARE_SIZE = WIDTH//BOARD_ROWS
CIRCLE_RADIUS = 60
CIRCLE_WIDTH = 15
LINE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = 55

# RBG : red, blue, green
Bg_color = (7,94,84)
line_color = (23,145,135)
CIRCLE_COLOR = (255,255,255)
CROSS_COLOR = (0,0,0)


screen = pygame.display.set_mode((WIDTH , HEIGHT))
pygame.display.set_caption("TIC TAC TOE")
screen.fill(Bg_color)

def draw_lines():
    #horizontal line 1
    pygame.draw.line(screen, line_color, (0,200), (600, 200), LINE_WIDTH)
    #horizontal line 2
    pygame.draw.line(screen, line_color, (0,400), (600, 400), LINE_WIDTH)
    #vertical line 1
    pygame.draw.line(screen, line_color, (200, 0), (200, 600), LINE_WIDTH)
    #vertical line 2
    pygame.draw.line(screen, line_color, (400, 0), (400, 600), LINE_WIDTH)

draw_lines()

board = np.zeros((BOARD_ROWS, BOARD_COL))
# print(board)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen,CIRCLE_COLOR, (int(col * 200 +100),int(row * 200 +100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col] ==2:
                pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE, row * 200 + 200- SPACE),(col * 200+ 200 - SPACE , row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE , row * 200 + SPACE),(col * 200 +200 - SPACE, row * 200 + 200- SPACE),CROSS_WIDTH)


def mark_square(row,col,player):
    board[row][col] = player


def available_square(row,col):
    return board[row][col] ==0


# #for checking if marked or not
def board_is_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    # vertical win check
    for col in range (BOARD_COL):
        if board[0][col] == player and board[1][col] == player and board[2][col]== player:
            draw_vertical_winning_line(col,player)
            return True


        # horizontal win check
    for row in range (BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True

        # asc win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

        # dsc win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_dsc_diagonal(player)
        return True
    return False


def draw_vertical_winning_line(col, player):
    posX = col * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(posX,15), (posX,HEIGHT -15), 15)

def draw_horizontal_winning_line(row,player):
    posY = row * 200 + 100
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color,(15 , posY), (WIDTH-15,posY),15)
def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen, color(15 , HEIGHT - 15),(WIDTH - 15, 15),15)
def draw_dsc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR
    pygame.draw.line(screen,color,(15,15), (WIDTH-15, HEIGHT - 15), 15 )
def restart():
    screen.fill(Bg_color)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COL):
            board[row][col] = 0


#
# # false coz board is not marked full
# print(board_is_full())


# # code for marking all squares in board
# for row in range(BOARD_ROWS):
#     for col in range(BOARD_COL):
#         mark_square(row,col,1)
#
# # true coz all squares are now marked
# # print(board_is_full())

player = 1
game_over = False
# MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0] #x
            mouseY = event.pos[1] #y

            clicked_row = int(mouseY // 200)
            clicked_col = int(mouseX // 200)

            # print(clicked_row)
            # print(clicked_col)

            if available_square(clicked_row,clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player ==2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        game_over = True
                    player = 1
                draw_figures()
                print(board)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()





    pygame.display.update()
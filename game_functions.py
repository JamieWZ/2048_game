import os
import random


def create_board():
    board = [[0 for i in range(4)] for j in range(4)]
    row_1 = random.randint(0, 3)
    col_1 = random.randint(0, 3)
    row_2 = random.randint(0, 3)
    col_2 = random.randint(0, 3)

    while row_1 == row_2 and col_1 == col_2:
        row_2 = random.randint(0, 3)
        col_2 = random.randint(0, 3)

    board[row_1][col_1] = 2
    board[row_2][col_2] = 2
    return board


def print_board(board):
    print('-'*41)
    for row in board:
        print('|', end='\t')
        for num in row:
            print(num, end='\t')
        print('|', end='')
        print()
    print('-' * 41)


def add_new_tile(board):
    add_new = False
    for row in board:
        for num in row:
            if num == 0:
                add_new = True
                break

    if add_new:
        row = random.randint(0, 3)
        col = random.randint(0, 3)
        while board[row][col] != 0:
            row = random.randint(0, 3)
            col = random.randint(0, 3)
        board[row][col] = 2


def move_up(board):
    transposed_board = transpose_board(board)
    score_added = move_left(transposed_board)
    result = transpose_board(transposed_board)

    for i in range(len(result)):
        for j in range(len(result[i])):
            board[i][j] = result[i][j]
    return score_added

def move_down(board):
    transposed_board = transpose_board(board)
    score_added = move_right(transposed_board)
    result = transpose_board(transposed_board)

    for i in range(len(result)):
        for j in range(len(result[i])):
            board[i][j] = result[i][j]
    return score_added


def move_left(board):
    score_added = 0
    #move zeroes
    move_zeroes(board)

    #merge
    for i in range(len(board)):
        for j in range(len(board[i]) - 1):
            if board[i][j] != 0 and board[i][j] == board[i][j + 1]:
                board[i][j] *= 2
                board[i][j + 1] = 0
                score_added += board[i][j]
    move_zeroes(board)
    return score_added


def move_right(board):
    for row in board:
        row.reverse()

    score_added = move_left(board)

    for row in board:
        row.reverse()
    return score_added

def move_zeroes(board):
    for i in range(len(board)):
        slow = 0
        for fast in range(len(board[i])):
            if board[i][fast] != 0:
                board[i][slow], board[i][fast] = board[i][fast], board[i][slow] #swap
                slow += 1


def transpose_board(board):
    rows = len(board)
    cols = len(board[0])

    new_board = [[0 for i in range(rows)] for j in range(cols)]

    for i in range(rows):
        for j in range(cols):
            new_board[j][i] = board[i][j]

    return new_board


def is_winner(board):
    for row in board:
        for num in row:
            if num == 2048:
                return True
    return False


def is_game_over(board):
    row = len(board)
    col = len(board[0])

    for i in range(row):
        for j in range(col):
            if board[i][j] == 0:
                return False
            if i < row - 1 and board[i][j] == board[i + 1][j]:
                return False
            if j < col - 1 and board[i][j] == board[i][j + 1]:
                return False

    return True


def clear_screen():
    os.system('cls')
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
    print('-'*21)
    for row in board:
        print('|', end='\t')
        for num in row:
            print(num, end='\t')
        print('|', end='')
        print()
    print('-' * 21)

def add_new_tile(board):
    pass
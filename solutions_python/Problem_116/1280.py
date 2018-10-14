#!/usr/bin/env python3

size = 4
placeholder = '.'
tomek = 'T'

n = int(input())

def test_lines(board, symbols):
    for i in range(size):
        line = True
        for j in range(size):
            if line and board[i][j] not in symbols:
                line = False
        if line:
            return True
    return False

def test_cols(board, symbols):
    for i in range(size):
        column = True
        for j in range(size):
            if column and board[j][i] not in symbols:
                column = False
        if column:
            return True
    return False

def test_diags(board, symbols):
    match = True
    for i in range(size):
        if match and board[i][i] not in symbols:
            match = False

    if match: return True

    match = True
    for i in range(size):
        if match and board[i][size - i -1] not in symbols:
            match = False

    if match: return True

    return False

def won(board, symbol='X'):
    test = set([symbol, tomek])

    if test_lines(board, test):
        return True

    if test_cols(board, test):
        return True

    if test_diags(board, test):
        return True

    return False

def full(board):
    for i in range(size):
        if placeholder in board[i]:
            return False
    return True

for i in range(n):
    board = []
    for j in range(size):
        board.append(input())
    try:
        input() # read empty line
    except EOFError:
        pass

    if won(board, 'X'):
        status = 'X won'
    elif won(board, 'O'):
        status = 'O won'
    elif full(board):
        status = 'Draw'
    else:
        status = 'Game has not completed'

    print('Case #{0}: {1}'.format(i + 1, status))

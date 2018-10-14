__author__ = 'deniskrut'

import sys

def checkRow(row_num, board, player):
    win = True
    for i in range(0, 4):
        win = win and (board[row_num][i] == player or board[row_num][i] == 'T')
    return win

def checkColumn(col_num, board, player):
    win = True
    for i in range(0, 4):
        win = win and (board[i][col_num] == player or board[i][col_num] == 'T')
    return win

def checkMainDiagonal(board, player):
    win = True
    for i in range(0, 4):
        win = win and (board[i][i] == player or board[i][i] == 'T')
    return win

def checkNotMainDiagonal(board, player):
    win = True
    for i in range(0, 4):
        win = win and (board[i][3 - i] == player or board[i][3 - i] == 'T')
    return win

def checkWin(board, player):
    win = False
    for i in range(0, 4):
        if win:
            break
        win = win or checkRow(i, board, player)
    for i in range(0, 4):
        if win:
            break
        win = win or checkColumn(i, board, player)
    if not win:
        win = win or checkMainDiagonal(board, player)
    if not win:
        win = win or checkNotMainDiagonal(board, player)
    return win

def checkCompletion(board):
    not_complete = False
    for i in range(0, 4):
        for j in range(0, 4):
            if not_complete:
                break
            not_complete = board[i][j] == '.'
    return not not_complete

def getResult(board):
    x_win = checkWin(board, 'X')
    o_win = checkWin(board, 'O')
    if x_win and not o_win:
        return "X won"
    if o_win and not x_win:
        return "O won"
    if x_win and o_win:
        return "Draw"
    complete = checkCompletion(board)
    if complete:
        return "Draw"
    else:
        return "Game has not completed"

t = int(sys.stdin.readline())

res = []

for i in range(0, t):
    board = []
    for i in range(0, 4):
        line = sys.stdin.readline()
        board.append(line)
    local_res = getResult(board)
    res.append(local_res)
    sys.stdin.readline()

for i in range(0, t):
    print "Case #" + str(i + 1) + ": " + res[i]
#!/usr/bin/python2

def won(player):
    return rows(player) or cols(player) or diag1(player) or diag2(player)

def rows(player):
    for i in range(0,4):
        if row(i,player):
            return True
    return False

def cols(player):
    for j in range(0,4):
        if col(j,player):
            return True
    return False

def row(i, player):
    for j in range(0,4):
        if board[i][j] not in [player,"T"]:
            return False
    return True

def col(j, player):
    for i in range(0,4):
        if board[i][j] not in [player,"T"]:
            return False
    return True

def diag1(player):
    for i in range(0,4):
        if board[i][i] not in [player,"T"]:
            return False
    return True

def diag2(player):
    for j in range(0,4):
        i = 3-j
        if board[i][j] not in [player,"T"]:
            return False
    return True

def evaluate(board):
    if won("X"):
        return "X won"
    if won("O"):
        return "O won"
    for i in range(0,4):
        for j in range(0,4):
            if board[i][j] == ".":
                return "Game has not completed"
    return "Draw"

lines = open("A-large.in").readlines()
num_cases = int(lines[0])
x = 1
y = 4
for n in range(0,num_cases):
    board = lines[x:y+1]
    #print board
    print "Case #{0}: {1}".format(n+1, evaluate(board))
    x += 5
    y += 5

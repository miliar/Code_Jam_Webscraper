#!/usr/bin/python

def winner(row):
    xs = 0
    os = 0
    ts = 0
    for thing in row:
        if thing == 'X':
            xs += 1
        elif thing == 'O':
            os += 1
        elif thing == 'T':
            ts += 1
    if (xs == 3 and ts == 1) or (xs == 4 and ts == 0):
        return 'X won'
    elif (os == 3 and ts == 1) or (os == 4 and ts == 0):
        return 'O won'
    return None

def result(board):
    for i in range(4):
        w = winner(board[i])
        if w is not None:
            return w
    for i in range(4):
        row = []
        for j in range(4):
            row.append(board[j][i])
        w = winner(row)
        if w is not None:
            return w
    d = [board[0][0], board[1][1], board[2][2], board[3][3]]
    w = winner(d)
    if w is not None:
        return w
    d = [board[0][3], board[1][2], board[2][1], board[3][0]]
    w = winner(d)
    if w is not None:
        return w

    for i in range(4):
        for j in range(4):
            if board[i][j] == '.':
                return 'Game has not completed'
    return 'Draw'

with open("input.txt") as f:
    nboards = int(f.readline())
    for i in range(0, nboards):
        board=[]
        board.append(f.readline())
        board.append(f.readline())
        board.append(f.readline())
        board.append(f.readline())
        f.readline()
        print "Case #{}:".format(i+1), result(board)
        

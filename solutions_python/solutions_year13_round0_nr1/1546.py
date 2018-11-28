#!/usr/bin/python

f = open("A-small-attempt0.in", "r")

T = int(f.readline())

out = open("A-small.out", "w")

outs = ["X won", "O won", "Draw", "Game has not completed"]

def checkRow(board):
    s = set()
    for row in board:
        for c in row:
            if c == "X" or c == "O":
                s.add(c)
            if c == ".":
                break
        else:
            if len(s) == 1:
                return 0 if s.pop() == "X" else 1

def checkCol(board):
    for i in range(len(board)):
        s = set()
        for j in range(len(board[i])):
            if board[j][i] == "X" or board[j][i] == "O":
                s.add(board[j][i])
            if board[j][i] == ".":
                break
        else:
            if len(s) == 1:
                return 0 if s.pop() == "X" else 1

def checkDia(board):
    s = set()
    for i in range(4):
        if board[i][i] in "XO.":
            s.add(board[i][i])

    if "." not in s and len(s) < 2:
        return 0 if s.pop() == "X" else 1

    s = set()
    for i in range(4):
        if board[i][4-i-1] in "XO.":
            s.add(board[i][4-i-1])
    if "." not in s and len(s) < 2:
        return 0 if s.pop() == "X" else 1



for i in range(T):
    board = []
    for j in range(4):
        board.append(f.readline().strip())

    print board

    output = "Case #%d: %s\n"

    done = False
    checks = [checkRow, checkCol, checkDia]
    for check in checks:
        r = check(board)
        if r is not None:
            out.write(output % (i+1, outs[r]))
            done = True
            break

    if not done:
        if "." in ''.join(board):
            out.write(output % (i+1, outs[3]))

        else:
            out.write(output % (i+1, outs[2]))

    f.readline()

out.close()
f.close()

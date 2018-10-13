#!/usr/bin/env python3

def check(seq):
    mark = ""
    for c in seq:
        if c == ".": return ""
        elif c != "T":
            if mark:
                if c != mark: return ""
            else: mark = c
    return mark

def status(board):
    for i in range(4):
        c = check(board[(4*i):(4*i + 4)])
        if c: return "{0} won".format(c)

    for i in range(4):
        c = check(board[i::4])
        if c: return "{0} won".format(c)

    c = check(board[0::5])
    if c: return "{0} won".format(c)
    c = check(board[3:13:3])
    if c: return "{0} won".format(c)
    if "." in board: return "Game has not completed"
    return "Draw"

fin  = open("A-large.in",  "r")
fout = open("A-large.out", "w")

T = int(fin.readline())

for t in range(1, T + 1):
    board = ""
    for _ in range(4): board += fin.readline().rstrip()
    fout.write("Case #{0}: {1}\n".format(t, status(board)))
    fin.readline()

fin.close()
fout.close()

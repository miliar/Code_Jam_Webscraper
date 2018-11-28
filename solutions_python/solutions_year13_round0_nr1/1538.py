#!/usr/bin/env python

row = 4
col = 4
def getState(matrix):
    hasEmpty = False
    # Check row
    for i in range(4):
        flag = matrix[i][0]
        if (matrix[i][1] == flag or matrix[i][1] == 'T') \
                and (matrix[i][2] == flag or matrix[i][2] == 'T') \
                and (matrix[i][3] == flag or matrix[i][3] == 'T'):
            if flag == "X":
                return "X won"
            if flag == "O":
                return "O won"
        for j in range(1,4):
            if matrix[i][j] == '.':
                hasEmpty = True
    # Check col
    for i in range(4):
        flag = matrix[0][i]
        if (matrix[1][i] == flag or matrix[1][i] == 'T') \
                and (matrix[2][i] == flag or matrix[2][i] == 'T') \
                and (matrix[3][i] == flag or matrix[3][i] == 'T'):
            if flag == "X":
                return "X won"
            if flag == "O":
                return "O won"
        for j in range(1,4):
            if matrix[j][i] == '.':
                hasEmpty = True
    # Check diagonal
    flag = matrix[0][0]
    if (matrix[1][1] == flag or matrix[1][1] == 'T') \
            and (matrix[2][2] == flag or matrix[2][2] == 'T') \
            and (matrix[3][3] == flag or matrix[3][3] == 'T'):
        if flag == "X":
            return "X won"
        if flag == "O":
            return "O won"

    flag = matrix[0][3]
    if (matrix[1][2] == flag or matrix[1][2] == 'T') \
            and (matrix[2][1] == flag or matrix[2][1] == 'T') \
            and (matrix[3][0] == flag or matrix[3][0] == 'T'):
        if flag == "X":
            return "X won"
        if flag == "O":
            return "O won"

    if hasEmpty:
        return "Game has not completed"
    else:
        return "Draw"

#f = open("small")
f = open("A-small-attempt0.in")
lines = f.readlines()

num = int(lines[0])

wfile = open("lk", "w")
index = 1
for i in range(num):
    matrix = []
    for j in range(index, index+4):
        ns = list(lines[j].strip())
        matrix.append(ns)

    wfile.write("Case #%d: %s\n" % (i+1, getState(matrix)))
    index += 5

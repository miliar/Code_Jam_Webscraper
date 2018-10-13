#!/usr/bin/env python

import sys

input = open(sys.argv[1], "r")
number = int(input.readline())
for n in range(0, number):
    board = [list(input.readline().strip()), list(input.readline().strip()), \
            list(input.readline().strip()), list(input.readline().strip())]
    input.readline()

    # Check which is the right situation
    msg = ""
    dot_flag = False
    for i in range(0, 4):
        for j in range(0, 4):
            if board[i][j] == ".":
                dot_flag = True
            
    for i in range(0, 4):
        horizontal = ""
        for j in range(0, 4):
            horizontal += board[i][j]
        if horizontal.replace("T", "X") == "XXXX":
            msg = "X won"
        if horizontal.replace("T", "O") == "OOOO":
            msg = "O won"

    for i in range(0, 4):
        vertical = ""
        for j in range(0, 4):
            vertical += board[j][i]
        if vertical.replace("T", "X") == "XXXX":
            msg = "X won"
        if vertical.replace("T", "O") == "OOOO":
            msg = "O won"

    diag0 = ""
    diag1 = ""
    for i in range(0, 4):
        diag0 += board[i][i]
        diag1 += board[i][3-i]
    if diag0.replace("T", "X") == "XXXX" or diag1.replace("T", "X") == "XXXX":
        msg = "X won"
    if diag0.replace("T", "O") == "OOOO" or diag1.replace("T", "O") == "OOOO":
        msg = "O won"

    if msg == "X won":
        print "Case #%d: X won" % (n+1)
    elif msg == "O won":
        print "Case #%d: O won" % (n+1)
    elif msg == "" and dot_flag == True:
        print "Case #%d: Game has not completed" % (n+1)
    else:
        print "Case #%d: Draw" % (n+1)
    
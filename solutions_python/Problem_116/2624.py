#!/usr/bin/python
import sys
from collections import Counter

input = open(sys.argv[1])
nentries = int (input.readline())

def processBoard(board):
    arrays = []
    for i in range(0,4):
        arrays.append(board[i]) #horizontal
    for i in range(0,4):
        arrays.append("".join([x[i] for x in board])) #vertical
    arrays.append("".join([board[0][0],board[1][1],board[2][2],board[3][3]]))
    arrays.append("".join([board[3][0],board[2][1],board[1][2],board[0][3]]))
    return arrays

def checkArrays(arrays):
    empty = False
    status = "Draw"
    for array in arrays:
        counter = Counter(array)
        x = counter['X']
        o = counter['O']
        t = counter['T']
        e = counter['.']

        if x == 4 or (x == 3 and t == 1):
            status = "X won"
            break
        elif o == 4 or (o == 3 and t == 1):
            status = "O won"
            break
        elif e > 0:
            empty = True

    if status == "Draw" and empty:
        status = "Game has not completed"
    return status
        

for i in range(0,nentries):
    board = []
    for j in range(0,4):
        board.append(input.readline())

    arrays = processBoard(board)
    status = checkArrays(arrays)
    print "Case #" + str(i+1) + ": " + status

    input.readline() # discard

#!/usr/bin/env python3

from functools import reduce
from operator import or_

T = int(input().strip())

for t in range(T):
    print("Case #{}: ".format(t + 1), end="")
    
    gridSize, modelCount = map(int, input().strip().split(" "))
    
    # You can't place two x-es in the same row or two +-es in the same diagonal
    # An o is just an x and a + combined
    xes = [[False for i in range(gridSize)] for j in range(gridSize)]
    pluses = [[False for i in range(gridSize)] for j in range(gridSize)]
    
    for i in range(modelCount):
        modelType, y, x = input().strip().split(" ")
        x, y = int(x) - 1, int(y) - 1
        if modelType == "+":
            pluses[y][x] = True
        elif modelType == "x":
            xes[y][x] = True
        elif modelType == "o":
            pluses[y][x] = True
            xes[y][x] = True
    
    original = tuple(tuple(zip(xrow, plusrow)) for xrow, plusrow in zip(xes, pluses))
    
    #fix up xes
    rowsUsed = [reduce(or_, row, False) for row in xes]
    colsUsed = [reduce(or_, col, False) for col in zip(*xes)]
    col = 0
    row = 0
    while True:
        while col < gridSize:
            if not colsUsed[col]:
                break
            else:
                col += 1
        else:
            break
        while row < gridSize:
            if not rowsUsed[row]:
                break
            else:
                row += 1
        else:
            break
        xes[row][col] = True
        row += 1
        col += 1
    
    #fix up pluses
    for i in range(gridSize):
        pluses[0][i] = True
    for i in range(1, gridSize - 1):
        pluses[-1][i] = True
    # naturally, this isn't general
    c = sum(map(sum, pluses)) + sum(map(sum, xes))

    solution = tuple(tuple(zip(xrow, plusrow)) for xrow, plusrow in zip(xes, pluses))
    changes = []
    for row in range(gridSize):
        for col in range(gridSize):
            if solution[row][col] != original[row][col]:
                modelType = "."
                if solution[row][col] == (True, False):
                    modelType = "x"
                elif solution[row][col] == (False, True):
                    modelType = "+"
                elif solution[row][col] == (True, True):
                    modelType = "o"
                changes.append("{} {} {}".format(modelType, row + 1, col + 1))
    print("{} {}".format(c, len(changes)))
    for line in changes: print(line)
    



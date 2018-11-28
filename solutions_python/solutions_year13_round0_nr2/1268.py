#! /usr/bin/python3

# Glen Robertson
# Lawnmower
# Code Jam Qualification Round 2013

def printGrid(grid, rows, cols, maxRows, maxCols):
    for row in range(rows):
        print(grid[cols * row : cols * (row+1)], maxRows[row])
    print()
    print(maxCols)
            

numCases = int(input().strip())
for case in range(numCases):
    rows, cols = map(int, input().strip().split())
    grid = []
    maxRows = []
    maxCols = []
    for row in range(rows):
        grid.extend(list(map(int, input().strip().split())))
        maxRows.append(max(grid[cols*row:cols*(row+1)]))
    for col in range(cols):
        maxCols.append(max(grid[col::cols]))
    
    ok = True
    for row in range(rows):
        if not ok:
            break
        for col in range(cols):
            if not (grid[cols * row + col] == maxRows[row] or
                    grid[cols * row + col] == maxCols[col]):
                ok = False
                break
    if ok:
        result = "YES"
    else:
        result = "NO"
    print("Case #" + str(case+1) + ":", result)

    #printGrid(grid, rows, cols, maxRows, maxCols)
            


    

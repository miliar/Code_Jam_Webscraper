from pylab import *

f = open("A-large.in", "r")
out = open("tic-large.out", "w")

def returnWinner(grid):
    x = winner('X',grid)
    o = winner('O',grid)
    if x and o:
        return "Draw"
    elif not x and not o:
        if not '.' in grid:
            return "Draw"
        else:
            return "Game has not completed"
    elif x:
        return "X won"
    elif o:
        return "O won"

def winner(player, grid):
    for row in range(4):
        if checkFour(player, grid[row,:]):
            return True
    for col in range(4):
        if checkFour(player, grid[:,col]):
            return True
    # up left to down right
    diag = []
    for i in range(4):
        diag.append(grid[i,i])
    if checkFour(player, diag):
        return True
    diag = []
    for i in range(4):
        diag.append(grid[3-i,i])
    if checkFour(player, diag):
        return True
    return False

def checkFour(player, lst):
    for i in range(4):
        if lst[i] != player and lst[i] != 'T':
            return False
    return True

t = int(f.readline())
for case in range(1, t+1):
    grid = empty([4,4], dtype=str)
    for i in range(4):
        line = f.readline()
        for c in range(4):
            grid[i,c] = line[c]
    out.write( "Case #%i: %s\n" %(case, returnWinner(grid)))
    f.readline()

out.close()
    

import sys

def check(gameboard):
    xWon = False
    yWon = False
    
    for i in range(4):
        xRow = True
        xCol = True
        yRow = True
        yCol = True
        for j in range(4):
            xRow = xRow and (gameboard[i][j] in ('X', 'T'))
            xCol = xCol and (gameboard[j][i] in ('X', 'T'))
            
            yRow = yRow and (gameboard[i][j] in ('O', 'T'))
            yCol = yCol and (gameboard[j][i] in ('O', 'T'))
        xWon = xWon or xRow or xCol
        yWon = yWon or yRow or yCol
    
    # check diagonals
    xDiag1 = True
    xDiag2 = True
    yDiag1 = True
    yDiag2 = True    
    for i in range(4):
        xDiag1 = xDiag1 and (gameboard[i][i] in ('X', 'T'))
        xDiag2 = xDiag2 and (gameboard[i][3-i] in ('X', 'T'))
        yDiag1 = yDiag1 and (gameboard[i][i] in ('O', 'T'))
        yDiag2 = yDiag2 and (gameboard[i][3-i] in ('O', 'T'))
        
    xWon = xWon or xDiag1 or xDiag2
    yWon = yWon or yDiag1 or yDiag2
    
    hasSpots = False
    for i in range(4):
        for j in range(4):
            hasSpots = hasSpots or (gameboard[i][j] == '.')
    
    if xWon:
        return "X won";
    elif yWon:
        return "O won";
    elif hasSpots:
        return "Game has not completed";
    else:
        return "Draw";

n = int(sys.stdin.readline())
for i in range(n):
    gameboard = []
    for j in range(4):
        gameboard.append(sys.stdin.readline().strip())
    sys.stdin.readline()
    print("Case #%d: %s" % (i + 1, check(gameboard)))    

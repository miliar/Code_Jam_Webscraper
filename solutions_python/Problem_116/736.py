inp = open('A-large.in')
oup = open('problemA-l.out','w')
numCases = int(next(inp))

def hasWon0(char, grid):
    for line in grid:
        for ch in line:
            if not (ch == char or ch == 'T' or ch == '\n'):
                break
        else:
            return True
    return False

def hasWon1(char, grid):
    for j in range(4):
        for i in range(4):
            if not (grid[i][j] == char or grid[i][j] == 'T' or grid[i][j] == '\n'):
                break
        else:
            return True
    return False

def hasWon2(char, grid):
    diag1 = ((0, 0),
             (1, 1),
             (2, 2),
             (3, 3))
    for cell in diag1:
        ch = grid[cell[0]][cell[1]]
        if not (grid[cell[0]][cell[1]] == char or ch == 'T' or ch == '\n'):
            return False
    else:
        return True

def hasWon3(char, grid):
    diag1 = ((3, 0),
             (2, 1),
             (1, 2),
             (0, 3))
    for cell in diag1:
        ch = grid[cell[0]][cell[1]]
        if not (grid[cell[0]][cell[1]] == char or ch == 'T' or ch == '\n'):
            return False
    else:
        return True

def hasWon(char, grid):
    if hasWon0(char, grid) or hasWon1(char, grid) or hasWon2(char, grid) or hasWon3(char, grid):
        return True
    return False

def hasCompleted(grid):
    for line in grid:
        for char in line:
            if char == '.':
                return False
    return True

for case in range(numCases):
    grid = []
    for line in range(4):
        grid.append(next(inp))
    next(inp)
    print grid
    xWin = oWin = False
    oup.write("Case #" + str(case + 1) + ": ")
    if hasWon('X', grid):
        xWin = True
    if hasWon('O', grid):
        oWin = True
    if oWin or xWin:
        if xWin and oWin:
            oup.write('Draw\n')
        elif xWin:
            oup.write('X won\n')
        elif oWin:
            oup.write('O won\n')
    elif hasCompleted(grid):
        oup.write('Draw\n')
    else:
         oup.write('Game has not completed\n')

oup.close()

__author__ = 'Mad Cow'


def TicTackToe(path):
    with open(path, 'r') as f:
        n_lines = 0
        n_cases = 1
        output = ''
        grid = ''
        for line in f:
            n_lines += 1
            if n_lines == 1:
                n_games = int(line.strip())
            else:
                grid = grid + line.strip();
                if n_lines%5 == 0:
                    output += "Case #" + str(n_cases) + ": " + Judge(grid)
                    n_cases += 1
                elif n_lines%5 == 1:
                    grid = ""
                    output += '\n'
    with open ('TTT.out', 'w') as f:
        f.write(output)


def Judge(grid):
    for i in range(4):
        result = JudgeAux(grid[4*i+0] + grid[4*i+1] + grid[4*i+2] + grid[4*i+3])
        if not result == 0:
            return Res(result)
        result = JudgeAux(grid[i] + grid[4+i] + grid[8+i] + grid[12+i])
        if not result == 0:
            return Res(result)
    result = JudgeAux(grid[0] + grid[5] + grid[10] + grid[15])
    if not result == 0:
        return Res(result)
    result = JudgeAux(grid[3] + grid[6] + grid[9] + grid[12])
    if not result == 0:
        return Res(result)
    return Draw(grid)

def JudgeAux(s):
    h = {'X':0, 'O':0, 'T':0, '.':0}
    for c in s:
        h[c] += 1
    if h['X'] + h['T'] == 4 and h['T'] < 2:
        return 1
    elif h['O'] + h['T'] == 4 and h['T'] < 2:
        return -1
    else:
        return 0

def Res(result):
    if result == 1:
        return 'X won'
    else:
        return 'O won'

def Draw(grid):
    h = {'X':0, 'O':0, 'T':0, '.':0}
    for c in grid:
        h[c] += 1
    if h['X'] + h['T'] + h['O'] == 16:
        return 'Draw'
    else:
        return 'Game has not completed'


TicTackToe('A-large.in')



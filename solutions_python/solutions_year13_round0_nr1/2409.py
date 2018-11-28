import sys

def combinations(player):
    return [player*4,player*3+'T',player*2+'T'+player,player+'T'+player*2,'T'+player*3]

def check_horizontal(player,i):
    line = ''
    for j in xrange(4):
        line += puzzle[i][j]
    return line in combinations(player)

def check_vertical(player,j):
    line = ''
    for i in xrange(4):
        line += puzzle[i][j]
    return line in combinations(player)

def check_diagonal1(player):
    line = ''
    for i in xrange(4):
        line += puzzle[i][i]
    return line in combinations(player)

def check_diagonal2(player):
    line = ''
    for i in xrange(4):
        line += puzzle[i][3-i]
    return line in combinations(player)

def print_state():
    contains_dot = False
    for i in xrange(4):
        if '.' in puzzle[i]:
            contains_dot = True
        if check_horizontal('X',i) or check_vertical('X',i) or check_diagonal1('X') or check_diagonal2('X'):
            return 'X won'
        if check_horizontal('O',i) or check_vertical('O',i) or check_diagonal1('O') or check_diagonal2('O'):
            return 'O won'
    if check_diagonal1('X'):
        return 'X won'
    if check_diagonal2('X'):
        return 'X won'
    if check_diagonal1('O'):
        return 'O won'
    if check_diagonal2('O'):
        return 'O won'
    return 'Game has not completed' if contains_dot else 'Draw'


if __name__=='__main__':
    fileName = sys.argv[1]
    with open(fileName+'.output','w') as fw:
        with open(fileName,'r') as fh:
            n = int(fh.readline())
            for i in xrange(n):
                puzzle = []
                for _ in xrange(4):
                    line = fh.readline()
                    puzzle.append(line)
                fw.write('Case #{0}: {1}\n'.format(i+1,print_state()))
                fh.readline()
            


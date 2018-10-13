import sys
import copy

def match(i):
    items = copy.copy(i)
    match_char = ' '
    matching = 0
    for i in items:
        if i == '.':
            return -1
        if i != 'T' and match_char == ' ':
            match_char = i
        if i == match_char or i == 'T':
            matching = matching + 1
    if (matching == 4):
        return match_char
    else:
        return 0

def getcolumn(p, c):
    return [p[0][c], p[1][c], p[2][c], p[3][c]]
    
def game(puzzle):
    a = [match(puzzle[0]), match(puzzle[1]), match(puzzle[2]), match(puzzle[3]),
        match(getcolumn(puzzle,0)),match(getcolumn(puzzle,1)),
        match(getcolumn(puzzle,2)), match(getcolumn(puzzle,3)),
        match([puzzle[0][0], puzzle[1][1], puzzle[2][2], puzzle[3][3]]),
    match([puzzle[3][0], puzzle[2][1], puzzle[1][2], puzzle[0][3]])]
    if (a.count('X') > 0):
        return "X won"
    if (a.count('O') > 0):
        return "O won"
    if (a.count(-1) > 0):
        return "Game has not completed"
    else:
        return "Draw"
    
puzzle = []
i = 1
for l in sys.stdin:
    if(len(l.strip()) == 4):
        puzzle.append(list(l.strip()))
        if len(puzzle) == 4:
            print "Case #" + str(i) + ": " + game(puzzle)
            puzzle = []
            i = i + 1
    

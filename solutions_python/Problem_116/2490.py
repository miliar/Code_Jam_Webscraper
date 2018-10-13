import sys, re

tseen = False

def check(s, v):
    global tseen
    if not tseen:
        tseen = v == 'T'
        return s == v or tseen
    return s == v

def horWin(s, l):
    c = 0
    for z in l:
        if check(s, z):
            
            c += 1 
    return s != '.' and c == 4

def verticalWin(s, c, b):
    i, w = 0, 0
    while i < 4:
        if check(s, b[i][c]):
            w += 1
        i += 1
    return s != '.' and w == 4

def diagWin(s, r, c, b):
    i, w = 0, 0
    if r == 0 and c == 0:
        return s != '.' and check(s, b[r+1][c+1]) and check(s, b[r+2][c+2]) and check(s, b[r+3][c+3])
    elif r == 0 and c == 3:
        return s != '.' and check(s, b[r+1][c-1]) and check(s, b[r+2][c-2]) and check(s, b[r+3][c-3])
    elif r == 3 and c == 0:
        return s != '.' and check(s, b[r-1][c+1]) and check(s, b[r-2][c+2]) and check(s, b[r-3][c+3])
    elif r == 3 and c == 3:
        return s != '.' and check(s, b[r-1][c-1]) and check(s, b[r-2][c-2]) and check(s, b[r-3][c-3])
    return False

def getWinner(case, b):
    global tseen
    tseen = False
    i, c, winner = 0, 0, 'D'
    while i < 4:
        c = 0 
        while c < 4:
            s = b[i][c]
            tseen = False
            if s == '.':
                winner = 'I'
                c += 1
                continue
            if horWin(s, b[i]):
                print 'Case #%d: %s won' % (case, s)
                return
            elif verticalWin(s, c, b):
                print 'Case #%d: %s won' % (case, s)
                return
            elif diagWin(s, i, c, b):
                print 'Case #%d: %s won' % (case, s)
                return
            c += 1
        i += 1
    if winner == 'I':
        print 'Case #%d: Game has not completed' % (case)
    elif winner == 'D':
        print 'Case #%d: Draw' % (case)

start, t, boards = True, 0, []
for line in sys.stdin.readlines():
    if len(line) > 0 and line != '\n':
        if start:
            t = int(line.strip())
            start = False
            b = []
        else:
            if len(b) == 4:
                boards.append(b)
                b = [ line.strip() ]
            else:
                b.append(line.strip())

boards.append(b)

i = 0
for i in xrange(len(boards)):
    getWinner(i + 1, boards[i])

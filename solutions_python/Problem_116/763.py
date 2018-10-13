import sys
from copy import deepcopy
#IMPORTANT: REMOVE \N FROM READLINE

f = sys.stdin

board = [[0 for x in range(4)] for x in range(4)]

def solve(b, sym):
    tab = deepcopy(b)
    for i in xrange(4):
        for j in xrange(4):
            if tab[i][j] == 'T': tab[i][j] = sym;
    for x in xrange(4):
        if (tab[x][0] == tab[x][1] == tab[x][2] == tab[x][3] == sym) :
            return True
    for y in xrange(4):
        if (tab[0][y] == tab[1][y] == tab[2][y] == tab[3][y] == sym) :
            return True
    if (tab[0][3] == tab[1][2] == tab[2][1] == tab[3][0] == sym):
        return True
    if (tab[0][0] == tab[1][1] == tab[2][2] == tab[3][3] == sym):
        return True

    return False

ngames = int(f.readline().strip())
for game in xrange(ngames):
    for x in xrange(4):
        line = f.readline().strip()
        for y in xrange(4):
            board[x][y] = line[y]
    wonx = solve(board,'X')
    wony = solve(board,'O')
    if (wonx and wony):
        print "Case #"+str((game+1))+": Draw"
    elif wonx:
        print "Case #"+str((game+1))+": X won"
    elif wony:
        print "Case #"+str((game+1))+": O won"
    else:
        count = 0
        for i in xrange(4):
            for j in xrange(4):
                if board[i][j] == '.': count = count + 1
        if count == 0:
            print "Case #"+str((game+1))+": Draw"
        else:
            print "Case #"+str((game+1))+": Game has not completed"
    line = f.readline()

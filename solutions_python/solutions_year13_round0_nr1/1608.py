"""A
   Google CodeJam 2013
"""

from datetime import datetime

import re

wins = [re.compile("^TTTT"),  #across
        re.compile("^....TTTT"),  #across
        re.compile("TTTT....$"),  #across
        re.compile("TTTT$"),  #across
        re.compile(".*T...T...T...T"),  #down
        re.compile("^T....T....T....T"),  #diagonal
        re.compile("^...T..T..T..T"),  #diagonal
       ]

def check(board):
    #print board
    for win in wins:
        if win.match(board):
            #print win.pattern, board
            return True
    return False

def routine(board):
    boardX = board.replace('X', 'T')
    x = check(boardX)
    if x:
        return "X won"

    boardO = board.replace('O', 'T')
    o = check(boardO)
    if o:
        return "O won"
    
    if '.' in board:
        return "Game has not completed"
    
    return "Draw"

if __name__ == '__main__':
    filename = "A-small-attempt1"  #A-large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        #N = [int(x) for x in f.readline().split()]
        
        board = ""
        for row in xrange(4):
            board += f.readline().strip()
        
        f.readline()
        
        #print N
        #print board

        print >>fo, "Case #%d: %s" % (case+1, routine(board))

    fo.close()
    f.close()
    print datetime.now()

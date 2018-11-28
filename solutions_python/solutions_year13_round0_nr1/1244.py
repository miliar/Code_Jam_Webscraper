#!/usr/bin/env python2.7

import numpy

def line(f):
    return f.readline().strip()

def winner(line):
    line=list(line)
    numT = line.count('T')
    if   line.count('X') + numT >= 4: return 'X'
    elif line.count('O') + numT >= 4: return 'O'
    else: return ''

def globalWinner(lines):
    for line in lines:
        if winner(line): return winner(line)
    return ''

with open('A-large.in') as f:
    for caseNum in range(int(line(f))):
        nextLine = line(f)
        if not nextLine: nextLine = line(f)
        board = numpy.array(
            [ list(x) for x in [nextLine,line(f),line(f),line(f)] ]
        )

        # print board
        testLines = []
        testLines += board
        testLines += board.transpose()
        testLines.append(board.diagonal())
        testLines.append(board[::-1].diagonal())


        print 'Case #{0}:'.format(caseNum+1),
        win = globalWinner(testLines)
        if not win:
            if '.' in board:    print 'Game has not completed'
            else:               print 'Draw'
        elif win == 'X':        print 'X won'
        elif win == 'O':        print 'O won'
        else:                   print 'OMGWTFBBQ'

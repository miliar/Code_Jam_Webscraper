#!/usr/bin/python

import sys
import numpy

def checkRow(row):
    row = list(row)
    t = row.count('T')
    if row.count('X') + t == 4:
        return ('X',0)
    if row.count('O') + t == 4:
        return ('O',0)
    return ('',row.count('.'))    
    
def checkMatrix(m):
    emptyCells = 0

    for rotation in range(2):
        m = numpy.rot90(numpy.array(m))

        # rows
        for n in range(4):
            (winner, empty) = checkRow(m[n])
            if winner:
                return "%s won" % (winner)
            else:
                emptyCells += empty

        # diagonals
        (winner, empty) = checkRow(m.diagonal())
        if winner:
            return "%s won" % (winner)
        else:
            emptyCells += empty


    if emptyCells > 0:
        return "Game has not completed"
    else:
        return "Draw"


if len(sys.argv)>=2:
    fileIn = sys.argv[1]
else:
    fileIn = 'A-small-attempt0.in'

with open(fileIn) as f:
    for case in range(int(f.readline())):
        # create matrix
        m = [list(f.readline().strip()),list(f.readline().strip()),list(f.readline().strip()),list(f.readline().strip())]

        print "Case #%d: %s" % (case+1, checkMatrix(m))
                
        f.readline() #empty line

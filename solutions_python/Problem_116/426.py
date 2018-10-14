#!/usr/bin/env python
# coding: utf8

import sys

DIMENSION = 4

class Lines(object):
    def __init__(self, lines):
        self.lines = lines[:]
        self.counter = 0
    #enddef
    
    def __call__(self):
        retval = self.lines[self.counter].strip("\n")
        self.counter += 1
        return retval
    #enddef
#endclass


class Board(object):
    def __init__(self, lines):
        self.rows = lines[:]
        self.cols = [""] * DIMENSION
        for i in xrange(DIMENSION):
            for one in self.rows:
                self.cols[i] += one[i]
            #endfor
        #endfor
        self.diagonals = [
            "".join(self.rows[i][i] for i in xrange(DIMENSION)),
            "".join(self.rows[DIMENSION - 1 - i][i] for i in xrange(DIMENSION))
        ]
        self.all = self.rows + self.cols + self.diagonals
    #enddef
    
    def solve(self):
        wasDot = False
        for one in self.all:
            if one in ("OOOO", "OOOT", "OOTO", "OTOO", "TOOO"):
                return "O won"
            elif one in ("XXXX", "XXXT", "XXTX", "XTXX", "TXXX"):
                return "X won"
            elif ("." in one):
                wasDot = True
            #endif
        #endfor
        
        if wasDot:
            return "Game has not completed"
        else:
            return "Draw"
        #endif
    #enddef
    
    def __str__(self):
        retval = "\nROWS: \n" + "\n".join(self.rows)
        retval += "\n\nCOLS: \n" + "\n".join(self.cols)
        retval += "\n\nDIAGONALS: \n" + "\n".join(self.diagonals)
        retval += "\n\nALL: \n" + "\n".join(self.all)
        retval += "\n\n"
        
        return retval
    #enddef
#endclass


lines = Lines(open(sys.argv[1], "r").readlines())
caseCount = int(lines())
for caseNumber in xrange(1, caseCount + 1):
    board = Board(list(lines() for i in xrange(DIMENSION)))

    # empty line
    lines()

    print "Case #%d:" % caseNumber,
    print board.solve()
#endfor




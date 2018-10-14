#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:    Vadim Zadorozhny <vadim.zadorozhny@gmail.com>
# Created:   13.04.13
#-------------------------------------------------------------------------------

from sys import stdin

class Board (object) :
    
    SIZE = 4
    
    def __init__ (self) :
        self.field = ''

    def read (self, infile) :
        self.field = ''.join ([infile.readline().strip() for i in range (self.SIZE)])
        return self
    
    def solve (self) :
        emptyFound = False
        for i in range (self.SIZE) :
            r = self.checkSlice (self.field [i*self.SIZE : (i+1)*self.SIZE])
            if r in ('X', 'O') :
                return "{} won".format (r)
            c = self.checkSlice (self.field [i : : self.SIZE])
            if c in ('X', 'O') :
                return "{} won".format (c)
            if '.' in (r, c) :
                emptyFound = True
        d1 = self.checkSlice (self.field [: : self.SIZE+1])
        d2 = self.checkSlice (self.field [self.SIZE-1 : -(self.SIZE-1) : self.SIZE-1])
        if d1 in ('X', 'O') :
            return "{} won".format (d1)
        if d2 in ('X', 'O') :
            return "{} won".format (d2)
        if '.' in (d1, d2) :
            emptyFound = True
        if emptyFound :
            return "Game has not completed"
        else :
            return "Draw"

    def checkSlice (self, slc) :
        check = lambda c : all ([fc in (c, 'T') for fc in slc])        
        if slc.find ('.') >= 0 :
            return '.'
        elif check ('X') :
            return 'X'
        elif check ('O') :
            return 'O'
        else :
            return False


def main () :
    inpfile = stdin
    totalCases = int (inpfile.readline().strip())
    for caseno in xrange (1, totalCases+1) :
        print "Case #{}: {}".format (caseno, Board().read(inpfile).solve())
        inpfile.readline()


if __name__ == "__main__" :
    main()
    

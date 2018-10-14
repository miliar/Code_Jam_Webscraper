#!/usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Author:    Vadim Zadorozhny <vadim.zadorozhny@gmail.com>
# Created:   13.04.13
#-------------------------------------------------------------------------------

from sys import stdin

class Lawn (object) :
    def __init__ (self) :
        self.n = 0
        self.m = 0
        self.field = []
        
    def read (self, infile) :
        size = infile.readline().strip().split (' ')
        self.n = int (size[0])
        self.m = int (size[1])
        for i in xrange (self.n) :
            self.field.extend (
                [int (a) for a in infile.readline().strip().split (' ')])
        return self
                
    def solve (self) :
        def mmax (iter) :
            print iter
            return max (iter)
        maxN = [max (self.field [rowno*self.m : (rowno+1)*self.m]) for rowno in xrange (self.n)]
        maxM = [max (self.field [colno : : self.m]) for colno in xrange (self.m)]
        for rowno in xrange (self.n) :
            for colno in xrange (self.m) :
                h = self.field [rowno * self.m + colno]
                if h < maxN [rowno] and h < maxM [colno] :
                    return False
        return True


def main () :
    inpfile = stdin
    totalCases = int (inpfile.readline().strip())
    for caseno in xrange (1, totalCases+1) :
        possible = Lawn().read(inpfile).solve()
        print "Case #{}: {}".format (caseno, "YES" if possible else "NO")
    

if __name__ == "__main__" :
    main()
    

#!/usr/bin/env python
# coding: utf8

import sys

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


class Lawn(object):
    def __init__(self, x, y, lines):
        self.lawn = []
        for i in xrange(x):
            self.lawn.append(tuple(int(one) for one in lines[i].split(" ")))
        #endfor
        
        self.x = x
        self.y = y
    #enddef
    
    def solve(self):
        for i in xrange(0, self.x):
            for j in xrange(0, self.y):
                current = self.lawn[i][j]
                
                # horizontal access
                access = True
                for l in range(0, j) + range(j + 1, self.y):
                    if current < self.lawn[i][l]:
                        #print "position", i, j, "not accessible horizontally on", i, l
                        access = False
                        break
                    #endif
                #endfor
                if access: continue
                
                # vertical access
                access = True
                for l in range(0, i) + range(i + 1, self.x):
                    if current < self.lawn[l][j]:
                        #print "position", i, j, "not accessible vertically on", l, j
                        access = False
                        break
                    #endif
                #endfor
                if access: continue
                
                return "NO"
            #endfor
        #endfor
        return "YES"
    #enddef
    
    def __str__(self):
        return str(self.lawn)
    #enddef
#endclass


lines = Lines(open(sys.argv[1], "r").readlines())
caseCount = int(lines())
for caseNumber in xrange(1, caseCount + 1):
    dimensions = tuple(int(one) for one in lines().split(" "))
    lawn = Lawn(dimensions[0], dimensions[1], tuple(lines() for i in xrange(dimensions[0])))
    print "Case #%d:" % caseNumber, 
    print lawn.solve()
#endfor




#!/usr/bin/python

import sys
from pprint import pprint
from collections import deque

TAB = '   '



def main(debug = False):
    if len(sys.argv) < 2:
        print 'no input file given!'
        return
    fin = open(sys.argv[1])
    T = int(fin.readline())
    for c in xrange(T):
        if debug: print "Case #%d:" % (c+1)
        N,L,H = [int(a) for a in fin.readline().split()]
        F = [int(a) for a in fin.readline().split()]
        if debug: print L, F, H
        
        p = None
        for a in xrange(H, L-1, -1):
            div = True
            for f in F:
                if (a % f) and (f % a):
                    div = False
                    break
            if div:
                p = a

        print "Case #%d:" % (c+1),
        if p == None:
            print 'NO'
        else:
            print p
                    
    fin.close()
                
                
if __name__ == '__main__':
    debug = False
    main(debug)
    

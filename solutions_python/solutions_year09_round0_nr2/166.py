#!/usr/bin/python

import sys, re
from numpy import *


def main():
    NN = int(sys.stdin.next())
    for nn in xrange(1,NN+1):
        print 'Case #%d:' % nn
        calculate()
        

def calculate():
    global R,C,t,ret,ch

    R,C = map(int, sys.stdin.next().split())
    t = []
    for r in range(R):
        t.append( map(int, sys.stdin.next().split()) )

    ret = zeros([R,C], dtype='uint8')

    ch = ord('a')
    
    for r in range(R):
        for c in range(C):
            label(r,c)
    
    ret = [' '.join(map(chr, r)) for r in ret]
    ret = '\n'.join(ret)
    print ret
    



DR = [-1, 0, 0, 1]
DC = [ 0,-1, 1, 0]
DRC = zip(DR,DC)

def label(r, c):
    global R,C,t,ret,ch

    if (not ret[r][c]):
        lowest = t[r][c]
        for dr,dc in DRC:
            nr = r + dr
            nc = c + dc
            if 0<=nr<R and 0<=nc<C and t[nr][nc]<lowest:
                lowest = t[nr][nc]
                lowr, lowc = (nr,nc)
        if lowest == t[r][c]:
            ret[r][c] = ch
            ch += 1
        else:
            ret[r][c] = label(lowr,lowc)
    return ret[r][c]
            
                

    
if __name__ == "__main__":
    main()

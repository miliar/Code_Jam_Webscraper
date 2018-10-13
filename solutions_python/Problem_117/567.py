#! /usr/bin/python

__author__ = 'Thomas "noio" van den Berg'

### IMPORTS ###
import sys
import numpy as np
from pprint import pprint


### FUNCTIONS ###    

def do(lawn):
    rowmax = lawn.max(axis=0)
    rowwise = lawn >= rowmax
    colmax = lawn.max(axis=1)
    colwise = (lawn.T >= colmax.T).T

    print rowwise
    print colwise

    possible = rowwise + colwise
    pall = possible.all()

    return "YES" if pall else "NO"



### PROCESS INPUT FILE ###

if __name__ == '__main__':
    f = open(sys.argv[1])
    fout = open(sys.argv[1].replace('.in','.out'),'w')

    T = int(f.readline())
    for case in xrange(T):
        N, M = [int(nm) for nm in f.readline().split()]
        lawn = [[int(p) for p in f.readline().strip().split()] for _ in xrange(N)]
        lawn = np.array(lawn)
        print lawn

        
        # print lawn.max(axis=1)


        
        ans = do(lawn)
        print ans
        fout.write('Case #%d: %s\n'%(case+1,ans))

#!/usr/bin/python
#
# a_tictactoetomek.py
#
# Sajjan Singh Mehta
# April 12, 2013

import numpy as np
import sys


N = 4


def findWin(x):
    if '.' in x:
        return ''
    
    x = np.unique(x)
    if len(x) == 1 or (len(x) == 2 and 'T' in x) :
        return x[0] if x[0] != 'T' else x[1]
    return ''

def testGrid(data):
    x = findWin([data[i][i] for i in xrange(N)]) 
    if x:
        return x +' won'
    else:
        x = findWin([data[i][N - i - 1] for i in xrange(N)])
        if x:
            return x +' won'

    for i in xrange(N):
        x = findWin(data[i,:])
        if x:
            return x +' won'
        else:
            x = findWin(data[:,i])
            if x:
                return x +' won'
    
    if not '.' in data:
        return 'Draw'
    return 'Game has not completed'

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    
    for i in xrange(1, T + 1):
        data = np.array([list(sys.stdin.readline().strip()) for j in xrange(N)])
        sys.stdin.readline()
        
        print 'Case #%d:' % i, testGrid(data)
    
    


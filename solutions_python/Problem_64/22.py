#!/bin/python

import sys
import math

inf = sys.stdin
T = int(inf.readline())
    
    
def isdirty(M, N, dirty, i, j, l):
    x = 2**l - 1
    x <<= (N-l-i)
    #print 'isdirty i=%d, j=%d, l=%d, mask=%x' % (i, j, l, x)
    for d in dirty[j:j+l]:
        #print 'checking: %x' % d
        #print 'd | x: %x' % (d | x)
        #print 'd ^ x: %x' % (d ^ x)
        if (d | x) != (d ^ x):
            #print 'yes, dirty', i, j, l
            return True
    #print 'clean', i, j, l
    return False
    
def setdirty(M, N, dirty, i, j, l):
    #print 'setdirty', i, j, l
    x = 2**l - 1
    x <<= (N-l-i)
    for k in range(j, j+l):
        dirty[k] |= x
    
def isboard(M, N, bark, i, j, l):
    #print 'isboard', i, j, l
    x = 2**l - 1
    x <<= (N-l-i)
    top = bark[j] & x
    check = top ^ (top << 1)
    expected = (2**(l-1) - 1) << (N-l-i+1)
    #print 'isboard i=%d, j=%d, l=%d, mask=%x, top=%x, shifted=%x, check=%x, exp=%x' % (i,j,l,x, top, top<<1, check, expected)
    if (check & expected) != expected:
        #print 'top fails board %x' % top
        return False
    
    expected = top ^ x
    for k in range(j+1, j+l):
        #print 'nextrow=%x, exp=%x, top=%x' % ((bark[k] & x), expected, top)
        if (bark[k] & x) != expected:
            #print 'nextrow fail'
            return False
        expected ^= x
    #print 'XXX XXX yesboard', i, j, l
    return True
    
    
for t in range(T):
    M, N = map(int, inf.readline().split())
    bark = []
    boards = [0] * (min(M, N) + 1)
    dirty = [0] * M
    for m in range(M):
        bark.append(int(inf.readline(), 16))
    for sz in range(min(M, N), 1, -1):
        #print 'looking for sz', sz
        for j in range(M-sz+1):
            #print 'starting i', i
            for i in range(N-sz+1):
                #print 'starting j', j            
                if not isdirty(M, N, dirty, i, j, sz):
                    if isboard(M, N, bark, i, j, sz):
                        boards[sz] += 1
                        setdirty(M, N, dirty, i,j, sz)
    
    #print M*N
    #print boards
    #print [i * b for i, b in enumerate(boards)]
    #print sum([i * b for i, b in enumerate(boards)])
    boards[1] = (M * N) - sum([i * i * b for i, b in enumerate(boards)])
    
    
    print 'Case #%d: %d' % (t+1, len([b for b in boards if b > 0]))
    for i in range(len(boards)-1, -1, -1):
        if boards[i] > 0:
            print i, boards[i]

#!/usr/bin/python

import sys

def TLBR( G, I ):
    r = 0
    c = 0
    top = R
    bottom = 0
    left = C
    right = 0
    while r < R:
        c = 0
        while c < C:
            if G[r][c] == I:
                top = min(top,r)
                bottom = max(bottom,r)
                left = min(left,c)
                right = max(right,c)
            c = c + 1
        r = r + 1
    return (top,left,bottom,right)

def brute( R, C, G ):
    r = 0
    c = 0
    
    while r < R:
        c = 0
        while c < C:
#            print r, c, G[r][c]
            if G[r][c] != '?':
                (top, left, bottom, right) = TLBR(G, G[r][c])
                i = top
                while i <= bottom:
                    j = left
                    while j <= right:
                        G[i][j] = G[r][c]
                        j = j + 1
                    i = i + 1

                # expand right
                done = False
                j = right + 1
                while not done and j < C:
                    i = top
                    for i in xrange(top,bottom+1):
                        if G[i][j] != '?':
                            done = True
                            break
                    if not done:
                        # fill
                        for i in xrange(top, bottom+1):
                            G[i][j] = G[r][c]
                        right = right + 1
                    j = j + 1
                # expand left
                done = False
                j = left - 1
                while not done and j >= 0:
                    i = top
                    for i in xrange(top,bottom+1):
                        if G[i][j] != '?':
                            done = True
                            break
                    if not done:
                        # fill
                        for i in xrange(top, bottom+1):
                            G[i][j] = G[r][c]
                        left = left -1 
                    j = j - 1
                # expand down
                done = False
                j = bottom + 1
                while not done and j < R:
                    for i in xrange(left,right+1):
                        if G[j][i] != '?':
                            done = True
                            break
                    if not done:
                        # fill
                        for i in xrange(left, right+1):
                            G[j][i] = G[r][c]
                        bottom = bottom + 1
                    j = j + 1
                # expand up
                done = False
                j = top - 1
                while not done and j >=0:
                    i = right
                    for i in xrange(left,right+1):
                        if G[j][i] != '?':
                            done = True
                            break
                    if not done:
                        # fill
                        for i in xrange(left, right+1):
                            G[j][i] = G[r][c]
                        top = top - 1
                    j = j - 1
            c = c + 1
        r = r + 1

    r = 0
    while r < R:
        print ''.join(G[r])
        r = r + 1

data = file(sys.argv[1]).read().splitlines()

NUMCASE = int(data.pop(0))

for CASE in xrange( 1, NUMCASE + 1 ):
    print 'Case #%d:' % ( CASE, ),
    (R, C) = [int(x) for x in data.pop(0).split()]
    G = []
#    print 
    for i in xrange(0,R):
        l = list(data.pop(0))
#        print ''.join(l)
        G.append(l)
    print
    brute( R, C, G )

        

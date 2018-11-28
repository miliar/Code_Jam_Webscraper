#! /usr/bin/env python

import sys
import re
f = open(sys.argv[1])
T = int(f.readline().strip())

for N in xrange(T):
    s = f.readline().strip()
    data = re.split("\s+",s)
    H, W = int(data[0]), int(data[1])
    
    m = []
    for row in xrange(H):
        l = re.split("\s+",f.readline().strip())
        m.append(map(lambda x:int(x), l))

    n = map(lambda x: ['0']*W, [0]*H)
    
    name = ord('a')

    for ni in xrange(H):
        for nj in xrange(W):

            i, j = ni, nj            
            path = []
            sink = False
            while n[i][j] == '0':
                v = m[i][j] #curr height
                curr = (i,j)
                # find next
                minv = v
                min = curr
                neighbor = [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]
                for nn in neighbor:
                    ii, jj = nn[0], nn[1]
                    if ii < 0 or ii >= H or jj < 0 or jj >= W:
                        continue
                    if m[ii][jj] < minv:
                        minv = m[ii][jj]
                        min = nn
                path.append(curr)
                if min == curr: #sink
                    sink = True
                    break
                else: i, j = min[0], min[1]
            # got out.. joined another lane?
            if sink: 
                label = chr(name)
                name += 1
            else: label = n[i][j]

            # label stuff in path
            for pp in path:
                n[pp[0]][pp[1]] = label

            
    # print ansewr
    print "Case #%d:"%(N+1)
    for row in n:
        line = ""
        for c in row:
            line += c + " "
        print line.strip()

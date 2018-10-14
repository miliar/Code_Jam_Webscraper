#!/usr/bin/env python

import sys

with open(sys.argv[1]) as f_in:
    lines = f_in.readlines()
    lines = [x.strip() for x in lines]

T = int(lines[0])

curpos = 1

def check(data):
    for n in range(0, N):
        for m in range(0, M):
            point = data[n][m]

            #print n, m
            #print [data[n][x] > point for x in range(0, M)]
            #print [data[x][m] > point for x in range(0, N)]

            if (
                any([data[n][x] > point for x in range(0, M)]) and
                any([data[x][m] > point for x in range(0, N)])
            ):
                #print data, "no because", n, m
                return "NO"

    return "YES"
                

for i in range(0, T):
    N, M = lines[curpos].split()
    N = int(N)
    M = int(M)
    data = []
    for j in range(0, N):
        newline = [int(x) for x in lines[curpos+1+j].split()]
        assert len(newline) == M
        data.append(newline)
    curpos += N+1

    print "Case #%d: %s" % (i+1, check(data))
    

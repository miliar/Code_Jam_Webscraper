#!/usr/bin/env python

import sys

ls = sys.stdin.readlines()

n = int(ls[0])
ls = ls[1:]

for i in range(n):
    nr, nc = [int(x) for x in ls[0].split()]
    ls = ls[1:]
    g = [list(x.strip()) for x in ls[:nr]]
    ls = ls[nr:]
    for r in range(nr):
        prev = -1
        for c in range(nc):
            if g[r][c] != '?':
                for cc in range(prev + 1, c):
                    g[r][cc] = g[r][c]
                prev = c
        if prev != -1:
            for cc in range(prev + 1, nc):
                g[r][cc] = g[r][prev]
    print "Case #%d:" % (i + 1)

    skip = 1
    for r in range(nr):
        if g[r][0] == '?':
            skip += 1
        else:
            for i in range(skip):
                print "".join(g[r])
            skip = 1
            last = r
    for i in range(skip - 1):
        print "".join(g[last])
            


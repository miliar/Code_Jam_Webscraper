#!/usr/bin/env python

import sys

# 0 = source
# 1 = sink

# 2 + i = r_i
# 2 + n + j = c_j

# 2 + i = a_i
# 2 + n + n + i = b_i

def init(n):
    s = []
    for i in range(n):
        s.append([])
        for j in range(n):
            s[i].append(0)
    return s

def dfs(cg, fg, seen, s, t, f):
    seen.add(s)
    if s == t:
        return f
    for i in range(0, len(cg)):
        if i not in seen and cg[s][i] > fg[s][i]:
            ff = dfs(cg, fg, seen, i, t, min(f, cg[s][i] - fg[s][i]))
            if ff > 0:
                fg[s][i] += ff
                fg[i][s] -= ff
                return ff
    return 0

ls = sys.stdin.readlines()
T = int(ls[0])
ls = ls[1:]
for C in range(T):
    n, m = [int(x) for x in ls[0].split()]
    ls = ls[1:]

    grid = init(n)
    
    xcap = init(2 + n + n) # r/c
    xflow = init(2 + n + n)
    pcap = init(2 + n + n + n + n) # diag
    pflow = init(2 + n + n + n + n)
    for i in range(n):
        xcap[0][2 + i] = 1
        xcap[2 + n + i][1] = 1
        for j in range(n):
            xcap[2 + i][2 + n + j] = 1
            pcap[2 + i + j][2 + n + n + (i - j + n - 1)] = 1

    for i in range(n + n - 1):
        pcap[0][2 + i] = 1
        pcap[2 + n + n + i][1] = 1

    points = m
    for i in range(m):
        t, r, c = ls[0].split()
        ls = ls[1:]
        r = int(r) - 1
        c = int(c) - 1
        grid[r][c] = t
        if t == 'o':
            points += 1
        if t == 'o' or t == 'x':
            xcap[0][2 + r] = 0
            xcap[2 + n + c][1] = 0
        if t == 'o' or t == '+':
            pcap[0][2 + r + c] = 0
            pcap[2 + n + n + (r - c + n - 1)][1] = 0

    seen = set()
    xs = 0
    while True:
        f = dfs(xcap, xflow, set(), 0, 1, 1000000)
        if f == 0:
            break
        xs += f

    seen = set()
    ps = 0
    while True:
        f = dfs(pcap, pflow, set(), 0, 1, 1000000)
        if f == 0:
            break
        ps += f

    xgrid = init(n)
    pgrid = init(n)
    new = 0
    for i in range(n):
        for j in range(n):
            if xflow[2 + i][2 + n + j] == 1:
                xgrid[i][j] = 1
            if pflow[2 + i + j][2 + n + n + (i - j + n - 1)] == 1:
                pgrid[i][j] = 1
            if (xgrid[i][j] + pgrid[i][j]) > 0:
                new += 1

    print "Case #%d: %d %d" % (C + 1, points + xs + ps, new)
#    print grid, xgrid, pgrid
    for i in range(n):
        for j in range(n):
            if xgrid[i][j] == 1 and (pgrid[i][j] == 1 or grid[i][j] == '+'):
                print "o %d %d" % (i + 1, j + 1)
            elif pgrid[i][j] == 1 and (xgrid[i][j] == 1 or grid[i][j] == 'x'):
                print "o %d %d" % (i + 1, j + 1)
            elif xgrid[i][j] == 1:
                print "x %d %d" % (i + 1, j + 1)
            elif pgrid[i][j] == 1:
                print "+ %d %d" % (i + 1, j + 1)

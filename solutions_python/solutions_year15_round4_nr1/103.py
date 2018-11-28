import os
import sys
import resource

resource.setrlimit(resource.RLIMIT_STACK, (65000000, 65000000))
sys.setrecursionlimit(200100)

dirs = [(0,1), (0,-1), (1,0), (-1,0)]
dirss = "><v^"

def in_mp(x, y):
    global n,m
    return 0 <= x < n and 0 <= y < m

def go(cx, cy, dx, dy):
    global no
    cx += dx
    cy += dy
    while in_mp(cx, cy):
        if no[cx][cy] != -1:
            return no[cx][cy]
        cx += dx
        cy += dy
    return -1


for cases in range(int(raw_input())):
    n, m = map(int, raw_input().split())
    mp = [raw_input() for x in range(n)]
    no = [[-1]*m for x in range(n)]

    ans = 0
    for i in range(n):
        for j in range(m):
            if mp[i][j] != '.':
                no[i][j] = 1

    IMPOSSIBLE = False
    
    for i in range(n):
        for j in range(m):
            if mp[i][j] != '.':
                d = dirss.index(mp[i][j])
                if go(i, j, dirs[d][0], dirs[d][1]) == -1:
                    ans += 1
                    for dx, dy in dirs:
                        if go(i, j, dx, dy) != -1:
                            break
                    else:
                        IMPOSSIBLE = True
    
    if IMPOSSIBLE:
        print "Case #%d: IMPOSSIBLE" % (cases+1)
    else:
        print "Case #%d: %d" %(cases+1, ans)


#!/usr/bin/python

import sys

NCASE = int(sys.stdin.readline())

def go(r,c,d):
    if d == '^':
        for r2 in xrange(r-1,-1,-1):
            yield (r2,c)
    if d == 'v':
        for r2 in xrange(r+1,R):
            yield (r2,c)
    if d == '<':
        for c2 in xrange(c-1,-1,-1):
            yield (r,c2)
    if d == '>':
        for c2 in xrange(c+1,C):
            yield (r,c2)

for case in range(1,NCASE+1):
    R,C = map(int, sys.stdin.readline().split())
    M = [ sys.stdin.readline().strip() for _ in xrange(R) ]

    ans = 0
    for r in xrange(R):
        for c in xrange(C):
            if M[r][c] == '.': continue
            d = M[r][c]
            if any( M[nr][nc]!='.' for (nr,nc) in go(r,c,d) ): continue
            for nd in "^v><":
                if nd!=d and any( M[nr][nc]!='.' for (nr,nc) in go(r,c,nd) ):
                    ans += 1
                    break
            else:
                ans = -1
                break
        if ans < 0:
            break

    print 'Case #%d: %s' % (case, str(ans) if ans>=0 else 'IMPOSSIBLE')

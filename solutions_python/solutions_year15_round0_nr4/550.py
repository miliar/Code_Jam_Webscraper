"""
Codejam 2015
"""
import sys

def hardsize(N):
    sizes = []
    r = N
    c = 1
    while r >= c:
        sizes.append((r, c))
        r -= 1
        c += 1
    return sizes

def n_omino(X, R, C):

    if X > R*C:
        return "RICHARD"

    if R < C:
        temp = C
        C = R
        R = temp

    sizes = hardsize(X)

    for size in sizes:
        if size[0] > R or size[1] > C:
            return "RICHARD"
        if X == 4 and C == 2:
            return "RICHARD"


    if (R*C)%X != 0:
        return "RICHARD"


    return "GABRIEL"

T = int(raw_input())
CASES = []
for i in xrange(T):
    x, r, c = [int(j) for j in raw_input().split()]
    CASES.append((x, r, c))

print >> sys.stderr, CASES

RESP = []
for i in xrange(T):
    print "Case #%s: %s" % (i+1, n_omino(*CASES[i]))



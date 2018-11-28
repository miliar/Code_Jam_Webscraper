from math import sqrt

def solve(L, P, C):
    #print "L,P,C, P/L, P / L > C" ,  L,P,C, P / L, P / L > C
    res = 0
    while P / L > C:
        res += 1
        L = sqrt(P*L)
        #print "bingo L, P / L",  L, P / L
    return res

import sys
f = open(sys.argv[1], 'r')
t = int(f.readline())
case = 0
while t>0:
    L, P, C = map(float, f.readline().split())
    t -= 1
    case += 1
    print "Case #%d: %s" % ( case, solve(L,P,C) )

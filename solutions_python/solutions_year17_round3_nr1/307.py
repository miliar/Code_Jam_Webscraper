import math
from decimal import *

def solve(test):
    N, K = map(int, raw_input().split())

    p = []

    mx = 0
    index = 0

    for i in xrange(N):
        p.append( map( int, raw_input().split() ) )
        
    p.sort(lambda a,b: -1 if b[0]*b[1] < a[0]*a[1] else 1)

    area = 0

    for i in xrange(K-1):
        area += p[i][1] * p[i][0] * 2
        if p[i][0] > mx:
            mx = p[i][0]

    best = 0

    for i in xrange(K-1, N):
        a = p[i][1] * p[i][0] * 2
        if p[i][0] > mx:
            a += p[i][0] * p[i][0] - mx * mx
        
        if a>best:
            best = a

    getcontext().prec = 28

    print Decimal(area + best + mx*mx) * Decimal(math.pi)


def create_array(*sizes):
   return [0 if len(sizes)==1 else create_array(*sizes[1:]) for x in xrange(sizes[0])]



import sys
sys.stdin = open(sys.argv[1] if len(sys.argv) > 1 else "sample.in")

for test in range(input()):
    print "Case #{}:".format(test+1),
    answer = solve(test)
    if answer != None:
        print answer



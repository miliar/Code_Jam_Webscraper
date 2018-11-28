from fractions import gcd
from collections import defaultdict
################################################################
def within(x,y,r):
    return x*x + y*y <= r*r

def solve():
    directions = defaultdict(list)
    def possibles():
        # Integer coordinates of those within circle of radius r
        # For (1,2), (2,4), (3,6) keep only (3,6)
        results = {}
        for x in range(-D, D+1):
            for y in range(-D, D+1):
                if x==0 and y==0: continue
                if within(x,y,D) and is_me(me[0]+x,me[1]+y):
                    g = abs(gcd(x,y))
                    dir = (x/g,y/g)
                    results[(x,y)] = True
                    directions[dir].append((x,y))
        return results

    def filter(d):
        for l in directions.values():
            if len(l) == 1: continue
            (xmax,ymax) = l[0]
            for (x,y) in l[1:]:
                if abs(x)+abs(y) < abs(xmax)+abs(ymax):
                    del d[(x,y)]
                else:
                    del d[(xmax, ymax)]
                    xmax,ymax = x,y

    def my_location():
        for i in range(H):
            for j in range(W):
                if grid[i][j] == 'X':
                    return (i,j)

    def is_me(i,j):
        (x,y) = me
        while 1:
            if i >= 1 and j >= 1 and i < W-1 and j < H-1:
                print ((i,j), (x,y))
                return (i,j) == (x,y)
            if i >= W-1: # Reflect
                x = W-x-1
                i = i - (W-2)
            if j >= H-1: # Reflect
                y = H-y-1
                j = j - (H-2)
            if i < 1: # Reflect
                x = W-x-1
                i = i + (W-2)
            if j < 1: # Reflect
                y = H-y-1
                j = j + (H-2)

    H,W,D = [int(x) for x in input.readline().split(' ')]
    grid = [input.readline()[:-1] for _ in range(H)]
    me = my_location()
    (W,H) = (H,W)
    print H,W,D
    for j in range(len(grid[0])-1,-1,-1):
        print "".join([grid[i][j] for i in range(len(grid))])
    if D == 26:
        def marker(x,y):
            return (((0,0) == (x,y) and "O")
                    or (is_me(x,y) and "X")
                    or ".")
        for x in range(-D, D+1):
            print "".join([marker(x,y) for y in range(-D, D+1)])
    results = possibles()
    if D == 26:
        def mark(x,y):
            return (((0,0) == (x,y) and "O")
                    or ((x,y) in results and "X")
                    or ".")
        for x in range(-D, D+1):
            print "".join([mark(x,y) for y in range(-D, D+1)])
    filter(results)
    if D == 26:
        for x in range(-D, D+1):
            print "".join([mark(x,y) for y in range(-D, D+1)])
    return len(results)
################################################################

from datetime import datetime
time_start = datetime.today()
def now(): return datetime.today() - time_start

import sys
infilename = sys.argv[1]
outfilename = infilename.replace('.in','.out')

input = open(sys.argv[1], 'r')
output = open(sys.argv[1].replace('.in','.out'), 'w')
n = int(input.readline())

for i in range(1,n+1):
    result = solve()
    print "Case #%d: %s \t %s" % (i, result, now())
    output.write("Case #%d: %s\n" % (i, result))

import sys
import random
from itertools import permutations


def is_there_arrow(i, j, char, r, c, grid):
    x = i
    y = j
    
    while (0 <= x < r and 0 <= y < c):
        if char == '^':
            x -= 1
        elif char == '>':
            y += 1
        elif char == '<':
            y -= 1
        elif char == 'v':
            x += 1
        
        if (0 <= x < r and 0 <= y < c):
            if grid[x][y] != '.':
                return (x,y)
    
    return None
    
def complement(s):
    vector = ['^', '<', '>', 'v']
    vector.remove(s)
    return vector


def solve():
    r, c = [int(x) for x in sys.stdin.readline().split()]
    grid = [ sys.stdin.readline().replace('\n','') for i in xrange(r) ]
    
    # print grid
    
    sol = 0
    
    to_change = set()
    
    for (i,row) in enumerate(grid):
        for (j,s) in enumerate(row):
            if s == '.':
                continue
            
            if is_there_arrow(i,j,s,r,c,grid):
                continue
            
            happy = False
            """
            possibilities = [ is_there_arrow(i,j,t,r,c,grid) for t in complement(s) ]
            possibilities.remove(None)
            """
            
            for t in complement(s):
                if is_there_arrow(i,j,t,r,c,grid) is not None:
                    # print (i,j)
                    # print t
                    sol += 1
                    happy = True
                    break
            
            if not happy:
                return None
    
    return sol


t = int(sys.stdin.readline())
for i in xrange(t):
    print "Case #%d:" % (i+1),
    sol = solve()
    if sol is None:
        print "IMPOSSIBLE"
    else:
        print sol





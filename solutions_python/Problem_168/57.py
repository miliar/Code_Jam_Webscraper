from __future__ import division

import os
import sys
from math import log, floor, ceil, sqrt, pi
#from random import randint, choice, shuffle
#from collections import defaultdict
#from heapq import heappush, heappop, heapify
#inf = 10**20

name = 'A-large'

directions = {'>' : (0,1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}
def _solve(rows, cols, grid):
    parent = {}
    res = 0

    def first(x,y,dx,dy):
        nx = x
        ny = y
        while True:
            nx = nx + dx
            ny = ny + dy
            if not (nx >= 0 and nx < rows and ny >= 0 and ny < cols):
                return None
            if grid[nx][ny] in directions:
                return (nx,ny)

    for x in range(rows):
        for y in range(cols):
            #print(x,y)
            z = grid[x][y]
            if z in directions:
                dx, dy = directions[z]
                f = first(x,y,dx,dy)
                if f == None:
                    for dx, dy in directions.values():
                        f = first(x,y,dx,dy)
                        if f != None:
                            res += 1
                            parent[(x,y)] = f
                            break
                    if (x,y) not in parent:
                        return 'IMPOSSIBLE'
                else:
                    parent[(x,y)] = f
    return res



def format(out):
    return out

def solve(*args, **kwargs):
    return format(_solve(*args, **kwargs))

print(solve(2, 1, ("^", "^")),1)
print(solve(2, 2, (">v", "^<")), 0)
print(solve(3, 3, ("...", ".^.", "...")), "IMPOSSIBLE")
print(solve(1, 1, (".",)), 0)
print(solve(4, 4, (".^..", ".><.", ".<.^", "v^^^")), 4)
#sys.exit(0)

os.system('cp /home/mama/Downloads/%s.in .'%name)
os.system('rm /home/mama/Downloads/%s*.in'%name)
lines = open('%s.in'%name).readlines()
output = open('%s.out'%name, 'w')
cases = int(lines[0])
curline = 1
for caseno in range(cases):
    r,c = tuple(int(x) for x in lines[curline].split())
    curline += 1
    inp = []
    for _ in range(r):
        inp.append(lines[curline].strip())
        curline += 1
    inp = tuple(inp)
    res = str(solve(r,c,inp))
    #print(inp, caseno, res)
    print('---')
    output.write('Case #%d: %s\n'%((caseno+1), res))
    output.flush()
output.close()
    









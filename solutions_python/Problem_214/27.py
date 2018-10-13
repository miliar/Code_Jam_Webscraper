import glob, pprint, pickle, os, time, sys
from copy import copy
from zope.interface.tests import odd
from numpy import array, sin, cos
import numpy as np
import itertools
import math
import itertools
import random
from collections import defaultdict

EMP = 0
WALL = 1
UD = 2
DU = 3
LASER = 4

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

VERTICAL = 0
HORIZONTAL = 1

def nextcoor(x,y,direction):
    if direction==UP:
        x-=1
    if direction==RIGHT:
        y+=1
    if direction==DOWN:
        x+=1
    if direction==LEFT:
        y-=1
    return x,y

def solve(R,C,grid):
    G = []
    lasers = 1
    L = []
    grid = [list(r) for r in grid]

    for x,g in enumerate(grid):
        row = []
        for y,c in enumerate(g):
            if c==".":
                row.append(EMP)
            elif c=="#":
                row.append(WALL)
            elif c=="/":
                row.append(DU)
            elif c=="\\":
                row.append(UD)
            elif c=="-" or c=="|":
                row.append(LASER)
                lasers+=1
                L.append((x,y))
        G.append(row)
    # print G
    orientations = [[True,True] for l in L]
    hittable = [[[] if G[r][c]==EMP else None for c in xrange(C)] for r in xrange(R)]

    for ln, laser in enumerate(L):
        for d,ori in [(UP,VERTICAL), (DOWN,VERTICAL), (RIGHT,HORIZONTAL), (LEFT,HORIZONTAL)]:
            x,y = laser
            x,y = nextcoor(x,y,d)
            while 0 <= x < R and 0 <= y < C:
                if G[x][y]==WALL:
                    break
                if G[x][y]==LASER:
                    orientations[ln][ori] = False
                if G[x][y]==EMP:
                    hittable[x][y].append((ln,ori))
                x,y = nextcoor(x,y,d)
    # print hittable

    system = []
    for r in hittable:
        for l in r:
            if l is not None:
                system.append(l)

    system.sort(key=len)
    print system
    # solve the system
    for ori in orientations:
        if ori[0] is False and ori[1] is False:
            return "IMPOSSIBLE"

    REM = "REM"
    while system:
        ns = []
        for s in system:
            # filter of what we know is impossible already
            s = [poss for poss in s if orientations[poss[0]][poss[1]] ]

            if len(s)==0:
                return "IMPOSSIBLE"
            if len(s)==1:
                l = s[0]
                if not orientations[l[0]][l[1]]:
                    return "IMPOSSIBLE"
                orientations[l[0]][l[1]] = True
                orientations[l[0]][1-l[1]] = False
            else:
                ns.append(s)

        system = ns
        for s in system:
            # filter of what we know is impossible already
            s = [poss for poss in s if orientations[poss[0]][poss[1]] ]
        system.sort(key=len)
        if system:
            if len(system[0])>1:
                l = system[0][0]
                orientations[l[0]][l[1]] = True
                orientations[l[0]][1-l[1]] = False
                for s in system:
                    # filter of what we know is impossible already
                    s = [poss for poss in s if orientations[poss[0]][poss[1]] ]

                system = system[1:]



        # print system
    for i,laser in enumerate(L):
        x,y = laser
        if orientations[i][0]:
            grid[x][y] = "|"
        elif orientations[i][1]:
            grid[x][y] = "-"
        else:
            return "IMPOSSIBLE"

    result = "\n".join(["".join(r) for r in grid])

    # print "t:",times
    return "POSSIBLE", "\n"+result

output = ""
TIC = time.time()
with open(sys.argv[1] if len(sys.argv) > 1 else "default.in") as f:
    def read_ints():
        return [int(x) for x in f.readline().strip().split(' ')]
    def read_frac():
        return [int(x) for x in f.readline().strip().split('/')]
    def read_strs():
        return [x for x in f.readline().strip().split(' ')]
    def read_floats():
        return [float(x) for x in f.readline().strip().split(' ')]

    (numquestions,) = read_ints()
    for questionindex in xrange(numquestions):

        ### calculate answer ###
        R,C = read_ints()
        grid = []
        for r in xrange(R):
            grid.append(read_strs()[0])
        answer = solve(R,C,grid)

        ### output ###
        answer_str = "Case #{}: {}".format(questionindex+1, " ".join([str(a) for a in answer]) if isinstance(answer, tuple) else answer)
        output += answer_str + '\n'
        print answer_str

ofile = open('output', 'w').write(output)
TOC = time.time()
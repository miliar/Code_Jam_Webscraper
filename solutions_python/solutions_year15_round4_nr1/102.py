__author__ = 'bszikszai'

from io import *

def pointsToOther(x, y, f, r, c):
    direction = (0, 0)
    cf = f[y][x]
    cp = (x, y)
    if cf == '^':
        direction = (0, -1)
    elif cf == '<':
        direction = (-1, 0)
    elif cf == '>':
        direction = (1, 0)
    elif cf == 'v':
        direction = (0, 1)
    isInside = True
    while isInside:
        cp = (direction[0] + cp[0], direction[1] + cp[1])
        isInside = cp[0] >= 0 and cp[0] < c and cp[1] >= 0 and cp[1] < r
        if (isInside):
            if f[cp[1]][cp[0]] != '.':
                return True
    return False

def getWalkoff(f, r, c):
    res = 0
    arrows = []
    crit = []
    for i in range(0, r):
        ctr = 0
        for j in range(0, c):
            if f[i][j] != '.':
                arrows.append((j, i))
                ctr += 1
        if (ctr == 1):
            crit.append(arrows[-1])
    while len(crit) > 0:
        ccrit = crit.pop()
        ctr = 0
        for i in range(0, r):
            if (f[i][ccrit[0]] != '.'):
                ctr += 1
        if ctr == 1:
            return "IMPOSSIBLE"
    while len(arrows) > 0:
        currentArrow = arrows.pop()
        nextArrow = pointsToOther(currentArrow[0], currentArrow[1], f, r, c)
        if not nextArrow:
            res += 1
    return res

def solve(f):
    r, c = [int(x) for x in f.readline().rstrip('\n').rstrip('\r').split(' ')]
    field = []
    for _ in range(0, r):
        field.append([x for x in f.readline().rstrip('\n').rstrip('\r')])
    return getWalkoff(field, r, c)

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))
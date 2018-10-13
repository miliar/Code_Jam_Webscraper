__author__ = 'bszikszai'

from io import *

def simulate(inp, round, maxlen):
    if round >= maxlen:
        return maxlen
    maxplate = max(inp)
    if maxplate <= 3:
        return round + maxplate
    maxpos = [i for i,j in enumerate(inp) if j == maxplate][0]
    movemin = []
    for moveCount in range(1, maxplate/2+1):
        newplates = list(inp)
        newplates[maxpos] -= moveCount
        newplates.append(moveCount)
        movemin.append(simulate(newplates, round + 1, maxlen))
    movemin.append(maxplate+round)
    return min(movemin)

def solve(f):
    f.readline()
    inp = [int(x) for x in f.readline().rstrip('\n').rstrip('\r').split(' ')]
    return simulate(inp, 0, max(inp))

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))
__author__ = 'bszikszai'

from io import *

def calc(v, x, s):
    minTemp = min([y[1] for y in s])
    maxTemp = max([y[1] for y in s])
    if x < minTemp or x > maxTemp:
        return "IMPOSSIBLE"
    if(len(s) == 1):
        return v / s[0][0]
    if (s[1][1] - s[0][1]) == 0:
        return v / (s[0][0] + s[1][0])
    v1 = (x * v - v * s[0][1])/(s[1][1]-s[0][1])
    v0 = (v - v1)
    return max(v0 / s[0][0], v1 / s[1][0])

def solve(f):
    row1 = [float(x) for x in f.readline().rstrip('\n').rstrip('\r').split(' ')]
    print row1[2]
    s = []
    for _ in range(0, int(row1[0])):
        s.append([float(x) for x in f.readline().rstrip('\n').rstrip('\r').split(' ')])
    return calc(row1[1], row1[2], s)

with open('input.txt', 'r') as f:
    with open('output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))
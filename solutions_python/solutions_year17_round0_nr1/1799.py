__author__ = 'bszikszai'

from io import *
import math

def simulate(s, k):
    i = 0
    f = 0
    while i <= (len(s)-k):
        if not s[i]:
            f += 1
            for j in range(i, i+k):
                s[j] = not s[j]
        i+=1
    for j in xrange(k):
        if not s[len(s)-j-1]:
            return "IMPOSSIBLE"
    return f


def solve(f):
    l =f.readline().rstrip('\n\r').split()
    s = [(c == '+') for c in l[0]]
    k = int(l[1])
    return simulate(s, k)

with open('17/1/A/input.txt', 'r') as f:
    with open('17/1/A/output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))
        print "Done"
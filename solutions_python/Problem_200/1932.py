__author__ = 'bszikszai'

from io import *
import math

def is_order(n):
    c = [ord(ch) for ch in str(n)]
    for i in xrange(len(c) - 1):
        if (c[i]>c[i+1]):
            return False
    return True

def simulate(n):
    d = [int(c) for c in str(n)]
    for i in xrange(len(d) - 1):
        if(d[i] > d[i+1]):
            for j in xrange(len(d) - i - 1):
                d[len(d) -j -1] = 9
            d[i] -= 1
            while (i > 0 and d[i-1] > d[i]):
                d[i] = 9
                i-=1
                d[i]-=1
    return "".join([str(c) for c in d]).lstrip("0")

def solve(f):
    inp = int(f.readline().rstrip('\n\r '))
    return simulate(inp)

with open('17/1/B/input.txt', 'r') as f:
    with open('17/1/B/output.txt', 'wb') as g:
        cases = int(f.readline())
        for i in range(0, cases):
            solution = solve(f)
            print "Case #%s: %s" % (i+1, solution)
            g.write("Case #%s: %s\n" % (i+1, solution))
        print "Done"
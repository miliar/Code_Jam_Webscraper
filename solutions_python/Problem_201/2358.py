import sys, math;
from collections import OrderedDict

def children(x):
    d = (x-1)/2
    a,b = math.ceil(d),math.floor(d)
    return [a,b]

def fast(n,k):
    i = 1
    c = children(n)
    o = OrderedDict()
    o[c[0]] = o.get(c[0], 0) + 1
    o[c[1]] = o.get(c[1], 0) + 1

    while i < k:
        top, topCount = o.popitem(last=False)
        jump = min(k-i,topCount)
        c = children(top)
        o[c[0]] = o.get(c[0], 0) + jump
        o[c[1]] = o.get(c[1], 0) + jump
        i += jump
    return c

def solveAll():
    f = sys.stdin
    cases = f.readline()
    for case in range(1, int(cases)+1):
        n, k = map(int, f.readline().split())
        a, b = fast(n, k)
        print("Case #{}: {} {}".format(case, a, b))

solveAll()



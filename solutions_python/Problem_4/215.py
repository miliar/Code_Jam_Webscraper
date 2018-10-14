import sys
from operator import add

inp = sys.stdin
num = int(inp.readline())

def scalar_pr(x, y):
    return reduce(add, map(lambda (x,y): x*y, zip(x,y)))

def all_perms(l):
    if len(l) <=1:
        yield l
    else:
        for perm in all_perms(l[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + l[0:1] + perm[i:]

for i in range(num):
    n = int(inp.readline())
    x = map(int, inp.readline().split())
    y = map(int, inp.readline().split())
    x.sort()
    y.sort()
    assert len(x) == len(y) == n
    m = None
    for q in all_perms(x):
        r = scalar_pr(q, y)
        if m is None or m > r:
            m = r
    print "Case #%d: %d" % (i+1, m)



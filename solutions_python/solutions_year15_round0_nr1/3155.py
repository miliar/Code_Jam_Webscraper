import numpy as np


def do():
    n, l = raw_input().split(' ')
    l = map(int, list(l))
    return max([0, max(map(lambda (i, n): i - n + 1, enumerate(np.cumsum(l))))])
T = int(raw_input())
for ti in xrange(1, T + 1):
    print "Case #{}: {}".format(ti, do())

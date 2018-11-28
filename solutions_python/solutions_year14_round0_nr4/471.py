__author__ = 'robertking'

from bisect import bisect_left
from sys import stdin
data = (line for line in stdin.read().splitlines())
T = int(next(data))
for case in range(1, T + 1):
    n = int(next(data))
    hers = map(float, next(data).split())
    his = map(float, next(data).split())
    his.sort()
    hers.sort()
    his2 = his[:]
    hers2 = hers[:]

    dw_points = 0
    for _ in range(n):
        if hers[-1] > his[0]:
            hers.pop(bisect_left(hers, his.pop(0)))
            dw_points += 1
        else:
            hers.pop(0)
            his.pop()

    w_points = 0
    for _ in range(n):
        if hers2.pop() > his2[-1]:
            his2.pop(0)
            w_points += 1
        else:
            his2.pop()
    print "Case #%d: %d %d" % (case, dw_points, w_points)


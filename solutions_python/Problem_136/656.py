__author__ = 'Alen'

import sys

N = int(sys.stdin.readline().strip())
for qw in range(1, N+1):
    print 'Case #%d:' % qw,

    line = sys.stdin.readline().strip().split(' ')
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    n = int(max(0.0, (X / C - 2.0 / F)))
    t = X / (2 + n * F)
    for i in range(n):
        t += C / (2 + i * F)
    print t
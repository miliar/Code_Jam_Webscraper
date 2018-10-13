import sys
import math
from collections import deque
import sets
import itertools
import copy

def is_tidy(n):
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            return False
    return True

def solve(xs):
    ok = -1
    for i in xrange(len(xs)-1, 0, -1):
        if xs[i] < xs[i-1]:
            xs[i-1] = xs[i-1] - 1
            for j in range(i, len(xs)):
                xs[j] = 9

    if xs[0] == 0:
        del xs[0]

T = int(sys.stdin.readline().strip())
for i in range(0, T):
    n = map(int, list(sys.stdin.readline().strip()))
    solve(n)
    print "Case #"+str(i+1)+": "+"".join(map(str, n))

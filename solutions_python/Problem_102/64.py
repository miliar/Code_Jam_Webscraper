import sys
import re
import math


T = int(sys.stdin.readline())

for i in range(T):
    js = [int(n) for n in sys.stdin.readline().split()][1:]
    N = len(js)
    X = sum(js)
    M = len([True for j in js if 2 * X <= j * N])
    L = sum([j for j in js if 2 * X <= j * N])
    
    sys.stdout.write('Case #{0}:'.format(i + 1))
    for j in js:
        if 2 * X <= j * N:
            sys.stdout.write(' 0')
        else:
            sys.stdout.write(' %.6f' % (100.0 * (2 * X - L - (N - M) * j) / (X * (N - M))))
#        sys.stdout.write(' %.6f' % (100.0 * (2 * X - N * j) / (X * N)))
    print()


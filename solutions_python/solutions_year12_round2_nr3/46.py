import sys
import re

def solve(ns):
    N = len(ns)
    def rec(depth, a, b):
        if sum(a) == sum(b) and len(a) > 0:
            return (a, b)
        if depth == N:
            return None
        r = rec(depth + 1, a, b)
        if r is None:
            r = rec(depth + 1, a + [ns[depth]], b)
        if r is None:
            r = rec(depth + 1, a, b + [ns[depth]])
        return r
    return rec(0, [], [])

T = int(sys.stdin.readline())

for i in range(T):
    ns = [int(n) for n in sys.stdin.readline().split()][1:]
    a = solve(ns)
    print('Case #{0}:'.format(i + 1))
    if a is None:
        print('Impossible')
    else:
        print(' '.join([str(n) for n in a[0]]))
        print(' '.join([str(n) for n in a[1]]))


# Core Training

import math

def solve(n, k, u, p):
    p.sort()
    ret = 0
    for i in range(1, len(p) + 1):
        p1 = min((sum(p[:i]) + u) / i, 1.0)
        prob = 1.0
        for pp in p[:i]:
            if pp > p1:
                prob = 0
            prob *= p1
        ret = max(ret, prob * reduce(lambda a, b: a * b, p[i:], 1.0))
    return ret

cases = int(raw_input())
for case in range(1, cases + 1):
    (n, k) = map(int, raw_input().split(' '))
    u = float(raw_input())
    p = map(float, raw_input().split(' '))
    print "Case #" + str(case) + ": " + str(solve(n, k, u, p))

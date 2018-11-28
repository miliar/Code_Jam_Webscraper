# Ample Syrup

import math

def solve(p, k):
    ret = 0
    for i in range(len(p)):
        (r1, h1) = p[i]
        a = []
        for j in range(len(p)):
            (r2, h2) = p[j]
            if i != j and r2 <= r1:
                a.append(2 * math.pi * r2 * h2)
        a = sorted(a, reverse=True)
        ret = max(ret, math.pi * r1 * r1 + 2 * math.pi * r1 * h1 + sum(a[:k - 1]))
    return ret

cases = int(raw_input())
for case in range(1, cases + 1):
    (n, k) = map(int, raw_input().split(' '))
    p = [map(int, raw_input().split(' ')) for i in range(n)]
    print "Case #" + str(case) + ": " + str(solve(p, k))

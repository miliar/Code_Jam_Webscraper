#!/usr/bin/env python
import sys
def solveCase(line):
    (C, F, X) = map(float, line.split())
    ans = X/2.0
    N = int(round(max((F*X - F*C - 2*C)/(F*C), 0.0) + 3.0))
    d=10
    MV = N+d+3
    R = range(max(0, N-d), N + d)
    reciprocals = [1.0/(2.0 + n*F) for n in range(0, MV)]
    for i in range(0, len(reciprocals)):
        if i == 0:
            cum = [reciprocals[0]]
        else:
            cum += [cum[i-1] + reciprocals[i]]
    for n in R:
        ans = min(ans, C*cum[n] + X*reciprocals[n+1])
    return ans

lines = [line.strip() for line in sys.stdin]
T = int(lines.pop(0))
assert len(lines) == T
for i in range(0, T):
    print "Case #{}: {}".format(i+1, solveCase(lines.pop(0)))

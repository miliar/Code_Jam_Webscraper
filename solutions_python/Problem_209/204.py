# 0th solution to Problem A
from math import pi

t = int(input())

def solve():
    best = -1
    n, k = map(int, input().split(' '))
    p = []
    for i in range(n):
        r, h = map(int, input().split(' '))
        p.append((r,h))
    p = sorted(p, key=lambda tup: (-tup[0], -tup[1]))
    for a in range(n-k+1):
        res = pi*(p[a][0]**2) + 2*pi*p[a][0]*p[a][1]
        p2 = p[a+1:]
        p2 = sorted(p2, key=lambda tup: -(tup[0]*tup[1]))
        for b in range(k-1):
            res += 2*pi* p2[b][0]*p2[b][1]
        best = max(best, res)

    return str(best)

for a0 in range(t):
    sol = solve()
    print("Case #" + str(a0 + 1) + ": " + sol)

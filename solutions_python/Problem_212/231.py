import sys
import numpy as np

filename = sys.argv[1]
f = open(filename)

cases = int(f.next())


class T:
    def __init__(self,a,b,c):
        self.st = a
        self.ed = b
        self.w = c

def solve():
    N,P = map(int, f.next().split())
    r = [0] * 5
    for i in range(N):
        k = int(f.next())
        r[k % P] += 1

    ans = 0

    if P == 2:
        ans += r[0]
        ans += (r[1] + 1) / 2

    if P == 3:
        ans += r[0]
        u = min(r[1], r[2])
        ans += u
        r[1] -= u
        r[2] -= u
        ans += (r[1] + 2) / 3
        ans += (r[2] + 2)/ 3

    if P == 4:
        ans += r[0]
        ans += r[2] / 2
        r[2] = r[2] % 2
        u = min(r[1], r[3])
        ans += u
        r[1] -= u
        r[3] -= u

        if r[2] > 0 and r[1] > 1:
            ans += 1
            r[2] -= 1
            r[1] -= 2

        if r[2] > 0 and r[3] > 1:
            ans += 1
            r[2] -= 1
            r[3] -= 2

        ans += (r[1] +3)/ 4
        ans += (r[2] + 3)/4

    return "%d"%ans

for i in range(1, cases+1):
    print("Case #%d: %s"%(i, solve()))
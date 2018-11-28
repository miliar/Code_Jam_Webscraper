# Google Code Jam 2010
# Qualification Round Problem B

import sys
import string

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

C = int(sys.stdin.readline())
for i in range(C):
    v = sys.stdin.readline().split()
    ts = []
    for s in v[1:]:
        ts.append(int(s))
    ts.sort()
    d = ts[1] - ts[0]
    for j in range(len(ts) - 2):
        d = gcd(d, ts[j+2] - ts[j+1])
    ans = ts[0] % d
    if ans != 0:
        ans = d - ans
    print("Case #%d: %d" % (i+1, ans))

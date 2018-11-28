import sys
from collections import defaultdict


T = int(sys.stdin.readline())

for t in xrange(T):
    line = sys.stdin.readline()
    N, K = line.split()
    N = int(N)
    K = int(K)

    gaps = defaultdict(int)
    gaps[N] = 1

    k = K - 1
    while k > 0:

        g = max(gaps.keys())
        
        c = 0
        if k > gaps[g]:
            c = gaps[g]
        else:
            c = k
        k -= c
            
        gaps[g] -= c
        if gaps[g] == 0:
            del gaps[g]

        if g % 2 == 0:
            gaps[g / 2] += c
            gaps[g / 2 - 1] += c
        else:
            gaps[g / 2] += c * 2

    g = max(gaps.keys())
    if g % 2 == 0:
        y = g / 2
        z = g / 2 - 1
    else:
        y = g / 2
        z = g / 2

    print("Case #%d: %d %d" % (t + 1, y, z))

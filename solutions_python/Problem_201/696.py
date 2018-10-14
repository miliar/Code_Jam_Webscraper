import sys

from bintrees import FastRBTree

T = int(sys.stdin.readline().strip())

def split(n):
    n -= 1
    return n // 2, n // 2 + (n % 2)

assert (0, 0) == split(1)
assert (0, 1) == split(2)
assert (1, 1) == split(3)

for t in range(1, T+1):
    N, K = map(int, sys.stdin.readline().strip().split())

    holes = FastRBTree({N: 1})

    while K > 0:
        size, count = holes.max_item()
        del holes[size]

        for s in split(size):
            holes[s] = holes.get(s, 0) + count
        
        K -= count

    minD, maxD = split(size)
    print("Case #%d: %d %d" % (t, maxD, minD))

    

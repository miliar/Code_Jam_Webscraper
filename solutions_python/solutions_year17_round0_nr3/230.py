import sys
from collections import defaultdict

def solveCase(t):
    N, K = map(int, sys.stdin.readline().split(" "))
    
    k = 1
    sizes = {N: 1}
    newSizes = defaultdict(int)
    
    while k < K:
        for size in sizes:
            if size != 0:
                newSizes[size / 2] += sizes[size]
                if size % 2 == 0:
                    newSizes[size / 2 - 1] += sizes[size]
                else:
                    newSizes[size / 2] += sizes[size]

                k += 2 * sizes[size]

        sizes = newSizes
        newSizes = defaultdict(int)

    k = k / 2
    L = None
    R = None
    for size in sorted(sizes.keys(), reverse=True):
        k += sizes[size]
        if k >= K:
            L = size / 2
            if size % 2 == 0:
                R = size / 2 - 1
            else:
                R = size / 2

            break
    
    print("Case #{}: {} {}".format(t, L, R))


T = int(sys.stdin.readline())

for i in range(T):
    solveCase(i + 1)

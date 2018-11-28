# Google codejam 2017B
# A. 

import math
import heapq
import functools
import operator

for t in range(1, int(input()) + 1):
    N, K= map(int, input().split())
    U = int(input().replace('.', ''))
    L = [int(e.replace('.', '')) for e in input().split()]
    #print(U, L)
    heapq.heapify(L)

    while U > 0:
        top = heapq.heappop(L)
        top += 1
        U -= 1
        heapq.heappush(L, top)

    #print(L)
    #print([e / 10000 for e in L])
    result = functools.reduce(operator.mul, [e / 10000 for e in L], 1)

    print ("Case #{}: {}".format(t, result))

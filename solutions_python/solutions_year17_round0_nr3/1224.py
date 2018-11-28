from heapq import *

T = int(input())

for i in range(T):
    n, k = map(int, input().split())

    q = []
    heappush(q, (-n, n, 1))

    while k > 0:
        order, size, cnt = heappop(q)

        if size % 2 == 1:
            val = size // 2
            heappush(q, (-val, val, cnt*2))
            low, high = val, val
        else:
            lval = size // 2
            rval = size // 2 - 1
            heappush(q, (-lval, lval, cnt))
            heappush(q, (-rval, rval, cnt))
            low, high = rval, lval
        k -= cnt

    print(f"Case #{i+1}: {high} {low}")
    

#0......0
#0..0...0
#0..0.0.0

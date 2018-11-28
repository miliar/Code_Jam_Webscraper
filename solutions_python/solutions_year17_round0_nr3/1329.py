from collections import Counter
from heapq import heappush, heappop
import math

for t in xrange(1, input()+1):
    N, K = map(int, raw_input().strip().split())

    heap = [-N]  # negate because heapq is a minheap, negate when popping
    counter = Counter({N: 1})

    while heap:
        size = -heappop(heap)
        many = counter.pop(size)

        half = (size - 1) / 2.0
        minspace = int(math.floor(half))
        maxspace = minspace if half.is_integer() else minspace + 1

        if K <= many:
            res = '{} {}'.format(maxspace, minspace)
            break

        else:
            if not counter[minspace]: heappush(heap, -minspace)
            counter[minspace] += many
            if not counter[maxspace]: heappush(heap, -maxspace)
            counter[maxspace] += many
            K -= many

    print 'Case #{}: {}'.format(t, res)

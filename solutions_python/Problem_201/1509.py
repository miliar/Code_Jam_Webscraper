t = int(raw_input())

# For each empty stall S, they compute two values LS and RS, each of which is 
# the number of empty stalls between S and the closest occupied stall to the 
# left or right, respectively

# Then they consider the set of stalls with the farthest closest neighbor, that
# is, those S for which min(LS, RS) is maximal. If there is only one such stall,
# they choose it; otherwise, they choose the one among those where max(LS, RS) 
# is maximal. If there are still multiple tied stalls, they choose the leftmost
# stall among those.

import heapq

for tt in xrange(t):
    n, k = map(int, raw_input().split())

    heap = []

    heapq.heappush(heap, -n)

    for i in xrange(k):
        curr = -heapq.heappop(heap)

        if (curr == 0):
            x = 0
            y = 0
        else:
            x = (curr - 1) // 2
            y = curr - 1 - x

        heapq.heappush(heap, -x)
        heapq.heappush(heap, -y)

    print 'Case #%d: %d %d' % (tt + 1, y, x)

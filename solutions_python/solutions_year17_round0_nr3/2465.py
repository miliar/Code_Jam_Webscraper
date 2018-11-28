from heapq import *

file = "C-small-1-attempt0.in.txt"
f = open(file, 'r')
T = int(f.readline().strip())

for i in range(T):
    N, K = [int(num) for num in f.readline().strip().split()]
    heap = []
    heappush(heap, -N)
    for j in range(K - 1):
        block = -heappop(heap)
        if block % 2 == 0:
            heappush(heap, -(block / 2))
            if block != 2:
                heappush(heap, -(block / 2 - 1))
        else:
            heappush(heap, -(block / 2))
            heappush(heap, -(block / 2))
    block = -heappop(heap)
    if block % 2 == 0:
    	m = block / 2 - 1
    	M = block / 2
    else:
    	m = block / 2
    	M = block / 2
    print "Case #%d: %d %d" % (i+1, M, m)

f.close()
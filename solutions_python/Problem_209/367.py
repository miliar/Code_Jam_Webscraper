from heapq import heappush, heappop
import copy
import math

# heap = []
# heappush(heap, 1)
# heappush(heap, 9)
# heappush(heap, 6)
# heappush(heap, 3)
# print heappop(heap)
# print heappop(heap)
# print heappop(heap)
# print heappop(heap)

T = int(raw_input())
for t in range(0, T):
    N, K = map(int, raw_input().split(' '))
    R = []
    H = []
    cake = []
    for n in range(0, N):
        r, h = map(int, raw_input().split(' '))
        R.append(r)
        H.append(h)
        cake.append((r, h))
    cake.sort(key=lambda x: x[0])
    heap = []
    # for i in range(0, K):
    #     heappush(heap, 2*cake[i][0]*cake[i][1])
    tmpMax = 0
    for i in range(0, N):
        if i >= K - 1:
            tmp = cake[i][0]*cake[i][0] + 2*cake[i][0]*cake[i][1]
            tmpHeap = copy.copy(heap)
            for j in range(0, K-1):
                tmp += -heappop(tmpHeap)
            if tmp > tmpMax:
                tmpMax = tmp
        heappush(heap, -2*cake[i][0]*cake[i][1])
    print "Case #" + str(t+1) + ": " + "{:.6f}".format(tmpMax*math.pi)

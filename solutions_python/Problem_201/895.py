import heapq
from math import ceil, floor
T = int(raw_input())

for case in range(1, T+1):
    # N = K = case
    N, K = map(int, raw_input().strip().split())
    S = [True] + [False] * N + [True]
    queue = []
    heapq.heappush(queue, -N * 1.0)

    max_l_r = 0
    min_l_r = 0
    for Ki in range(K):
        best = -heapq.heappop(queue)
        L = ceil(best / 2) - 1
        R = floor(best / 2)
        heapq.heappush(queue, -L)
        heapq.heappush(queue, -R)
        max_l_r = int(max(L, R))
        min_l_r = int(min(L, R))
        # print Ki+1, L, R
    print "Case #{}: {} {}".format(case, max_l_r, min_l_r)
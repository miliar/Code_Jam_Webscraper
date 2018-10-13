import sys
import numpy as np
import math
import heapq

def greedy(pancakes, N, K):
    #print("pancakes=", pancakes)
    pancakes.sort(key=lambda x: x[0], reverse=True)
    #print("pancakes=", pancakes)
    
    maxarea = 0
    for startidx in range(N-K+1):
        currarea = pancakes[startidx][0]*pancakes[startidx][0] + 2*pancakes[startidx][0]*pancakes[startidx][1]
        #choose K-1 contributing highest depth
        minheap = []
        for idx in range(startidx+1, N):
            heapq.heappush(minheap, 2*pancakes[idx][0]*pancakes[idx][1])
            if len(minheap) > K-1:
                heapq.heappop(minheap)
        for elem in minheap:
            currarea += elem
        maxarea = max(maxarea, currarea)
    
    return maxarea*math.pi
    
T=int(sys.stdin.readline())
for t in range(1, T+1):
    line=sys.stdin.readline()
    [N, K]=map(int, line.split())
    #print("N=", N, "K=", K)
    pancakes = []
    for _ in range(N):
        line=sys.stdin.readline()
        [Ri, Hi]=map(int, line.split())
        pancakes.append((Ri, Hi))
    #print("pancakes=", pancakes)
    res = greedy(pancakes, N, K)
    print("Case #%d: %.10f" % (t, res))

#!/bin/python
from heapq import *

T = int(input())

for i in range(T):
    D = int(input())
    data = [-int(j) for j in input().split()]
    heapify(data)
    data_copy = data[:]
    best = data[0]
    max_value = -best - 1
    for y in range(1, max_value):
        cnt = 0
        while -(data[0]) > y:
            max_cur = heappop(data)
            heappush(data, max_cur+y)
            heappush(data, -y)
            cnt += 1
            best = max(best, data[0] - cnt)
        data = data_copy[:]
    

    print("Case #%d: %d" % (i+1, -best))

#! /bin/python

from sys import stdin
from heapq import heappush, heappop


T = int(stdin.readline().strip())

for t in range(T):
    (N, K) = [int(x) for x in stdin.readline().split()]

    heap = [-1*N]
    state = {N:1}
    remains = K

    while True:
        n = heappop(heap)
        n = -n
        i = state[n]

        max = n//2
        min = (n-1)//2

        if remains <= i:
            print("Case #{}: {} {}".format(t+1, max, min))
            break

        remains -= i

        if max > 0:
            if max in state:
                state[max] += i
            else:
                state[max] = i
                heappush(heap, -max)
        if min > 0:
            if min in state:
                state[min] += i
            else:
                state[min] = i
                heappush(heap, -min)

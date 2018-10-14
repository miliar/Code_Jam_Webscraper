#!/usr/bin/python3

import sys, heapq

def maxheappush(heap, item):
    heapq.heappush(heap, 0-item)

def maxheappop(heap):
    return 0-heapq.heappop(heap)

T = input ()

for Tc in range (1, int(T)+1):

    Nstr, Kstr = input().split()
    N = int (Nstr)
    K = int (Kstr)

    h = []
    maxheappush (h , N)

    for k in range (K-1):

        m = maxheappop (h)

        ls = int ((m-1)/2)
        rs = int (m/2)

        if ls > 0:
            maxheappush(h, ls)
        if rs > 0:
            maxheappush(h, rs)


    m = maxheappop (h)
    
    ls = int ((m-1)/2)
    rs = int (m/2)

    print("Case #" + str(Tc) + ": " + str(rs) + " " + str(ls))


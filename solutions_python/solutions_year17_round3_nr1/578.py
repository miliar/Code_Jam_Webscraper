#!/usr/bin/env python3

import math
 
for i in range(int(input().strip())):
    n, k = map(int,input().strip().split())
    pcs = []
    for _ in range(n):
        r, h = list(map(int, input().strip().split()))
        pcs.append((h*2*r*math.pi, r*r*math.pi))
    pcs.sort()
    pcs = list(reversed(pcs))
    rs = [r for h, r in pcs]
    h_sum = 0
    max_h_sum = 0
    for h, r in pcs[:k-1]:
        h_sum += h
    max_h_sum = h_sum + pcs[k-1][0] + max(rs[:k])
    for (h, r) in pcs[k:]:
        max_h_sum = max(max_h_sum, h_sum + h + r)
    print("Case #{}: {}".format(i+1, max_h_sum))


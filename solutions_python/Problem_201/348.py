# -*- coding: utf-8 -*-
# @Author: Pandarison
# @Date:   2017-04-08
# @Last Modified time: 2017-04-08
from queue import PriorityQueue

T = int(input())
for case_id in range(1, T+1):
    N, K = map(int, input().split())
    t = K
    large = [N, 1]
    small = [N, 0]
    while True:
        #print(t, large, small)
        if t > large[1] + small[1]:
            t -= (large[1] + small[1])
            if large[0]%2==0:
                newLarge = large[1]
                newSmall = small[1]*2 + large[1]
            else:
                newLarge = large[1]*2 + small[1]
                newSmall = small[1]
            large[0] = large[0]//2
            small[0] = large[0]-1
            large[1] = newLarge
            small[1] = newSmall
            
        else:
            if t <= large[1]:
                L = (large[0]+1)//2 - 1
                R = large[0]//2
            else:
                L = (small[0]+1)//2 - 1
                R = small[0]//2
            break
    print("Case #%d: %d %d"%(case_id, max([L,R]), min([L, R])))

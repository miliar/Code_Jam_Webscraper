#!/usr/bin/env python3

import sys
import math

def solve():
    n, k = map(int, input().split())
    r = [0] * n
    h = [0] * n
    maxtime = 0
    for i in range(n):
        r[i], h[i] = map(int, input().split())
    max_by_r = list(range(n))
    max_by_rh = list(range(n))

    max_by_r.sort(key=lambda i:-r[i])
    max_by_rh.sort(key=lambda i:-(r[i]*h[i]))

    top_rh = 2 * sum(r[i]*h[i] for i in max_by_rh[:k-1])
    top_rh_ids = set(max_by_rh[:k-1])
    if k == 1:
        top_rh = 0
        top_rh_ids = set()

    #print(top_rh)
    #print(top_rh_ids)
    #print(max_by_r)

    cur = 0
    for i in max_by_r:
        if i in top_rh_ids:
            #print("found top rh")
            cur = max(cur, top_rh + 2 * r[max_by_rh[k-1]]*h[max_by_rh[k-1]] + r[i]*r[i])
            break
        else:
            #print("ok...")
            cur = max(cur, top_rh + 2 * r[i]*h[i] + r[i]*r[i])
    
    return cur * math.pi



def main():
    k = int(input())
    for i in range(k):
        print("Case #{}: {}".format(i + 1, solve()))

if __name__ == '__main__':
    main()

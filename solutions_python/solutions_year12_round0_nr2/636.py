#!/usr/bin/env python

t = int(input())
for case in range(1,t+1):
    nums = tuple(map(int,input().strip().split()))
    n,s,p = nums[:3]
    scores = sorted(nums[3:])
    total = 0
    for i in scores:
        div, rem = i//3, i % 3
        if p == 0:
            total += 1
            continue
        elif i == 0:
            continue
        if rem == 0:
            if div >= p:
                total += 1
            elif div == p-1 and s > 0:
                s -= 1
                total += 1
        elif rem == 1 and div+1 >= p:
                total += 1
        elif rem == 2:
            if div+1 >= p:
                total += 1
            elif div == p-2 and s > 0:
                s -= 1
                total += 1

    print('Case #{}: {}'.format(case,total))

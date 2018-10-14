#!/usr/bin/env python
# -*- coding: utf-8 -*-

T = int(input())
for i in range(T):
    num, audiences = input().split()
    audiences = list(map(int,list(audiences)))
    ans = 0
    stands = 0
    for j in range(len(audiences)):
        if audiences[j] != 0 and stands < j:
            ans += j - stands
            stands = j
        stands += audiences[j]


    print("Case #{0}: {1}".format(i+1,ans))

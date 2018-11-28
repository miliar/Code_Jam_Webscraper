#!/usr/bin/env python3
#-*- coding: utf-8 -*-
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
f = open("input.txt","r")
T = int(f.readline())
for i in range(T):
    nums = f.readline().split()
    nums = [int(x) for x in nums]
    diff = [abs(nums[k+1] - nums[k]) for k in range(1,len(nums)-1)]
    diff.sort()
    #print(diff)
    res = 0
    for j in range(0,len(diff)):
        res = gcd(res,diff[j])
    if res == 1:
        print("Case #",i+1,": ",0, sep="")
    else:
        print("Case #",i+1,": ",(res-(nums[1]%res))%res, sep="")

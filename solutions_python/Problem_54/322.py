#!/usr/bin/env python

import sys,fractions

data = " ".join(sys.stdin.readlines())
data = data.replace("\n","")
data = data.split(" ")
T = int(data[0])
data = data[1:]
for i in range(T):
    N = int(data[0])
    data = data[1:]
    nums = []
    for j in range(N):
        nums.append(int(data[0]))
        data = data[1:]
    a = min(nums)
    num2 = []
    for item in nums:
        if (item-a > 0):
            num2.append(item-a)
    while(len(num2)>1):
        num2.append(fractions.gcd(num2[0],num2[1]))
        num2 = num2[2:]
    a %= num2[0]
    a = num2[0]-a
    a %= num2[0]
    print "Case #%d: %d" % (i+1,a)

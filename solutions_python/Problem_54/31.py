#!/usr/bin/python

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

ntest = input()
for t in range(ntest):
    nums = sorted([int(x) for x in raw_input().split()[1:]])
    maxdiv = nums[1]-nums[0]
    for i in range(len(nums)-1):
        maxdiv = gcd(maxdiv, nums[i+1]-nums[i])
    print "Case #%d: "%(t+1) + str(maxdiv*((nums[0]+maxdiv-1)/maxdiv) - nums[0])

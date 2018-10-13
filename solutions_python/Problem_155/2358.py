#!/usr/bin/python

import sys


def getFriends(arr):
    standing_so_far = 0
    needed = 0
    for i in xrange(len(arr)):
        if(standing_so_far >= i):
            standing_so_far += arr[i]
        else:
            needed += i - standing_so_far
            standing_so_far = standing_so_far + (i-standing_so_far) + arr[i]
        #print needed, standing_so_far

    return needed
        


T = int(sys.stdin.readline())

for i in xrange(T):
    line = sys.stdin.readline().split(" ")
    arr = [c for c in line[1]]
    nums = map(int, arr[0:len(arr)-1])
    print "Case #%d:" %(i+1),
    print getFriends(nums)
    #print nums

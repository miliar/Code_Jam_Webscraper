#!/usr/bin/python

import sys



def find(num):
    l = len(num)
    i=l-1
    while i>0:
        if num[i-1] > num[i]:
            #print i, "less"
            for j in range(i, l):
                num[j] = '9'
            num[i-1] =  str(int(num[i-1]) - 1)
        i -= 1
        #print i, num
    for i in range(0,l):
        if num[i] != '0':
            return num[i:]
    return num


tc = raw_input()

nums = []

for line in sys.stdin.readlines():
    nums.append(list(line.strip()))

for i in range(0, len(nums)):
    #print a, len(a)
    print "Case #%s: %s" % (i+1, ''.join(find(nums[i])))


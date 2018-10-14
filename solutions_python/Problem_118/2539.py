#!/usr/bin/python
import sys
from math import log10
from math import sqrt
from math import pow
f = open('fair.txt', 'r')
first = int(f.readline())
#print "%d Case" % first
def sqrtc(x):
    ans = 0
    if x >= 0:
        while ans*ans < x:
            ans = ans + 1

        if ans*ans != x:  # this if statement was nested inside the while
            return None
        else:
            return ans
def rev(num):
    def rec(num, tens):
        if num < 10:
            return num        
        else:
            return num % 10 * tens + rec(num // 10, tens // 10)
    return rec(num, 10 ** int(log10(num)))

count = 0
for line in f:
    A = 0
    B = 0
    result = 0
    ints = [long(i) for i in line.split()]
    A,B = ints[0],ints[1]

    while A <= B:
        re = rev(A)
        if (sqrtc(A) and A == re):
            sqa = sqrt(A)
            re_s = rev(sqa)
            if  re_s == sqa:
                result += 1
        A +=1
    count += 1
    print "Case #%d: %d" % (count,result)

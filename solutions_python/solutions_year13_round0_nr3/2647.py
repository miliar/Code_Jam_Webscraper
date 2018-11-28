#!/usr/bin/python

import math

num=None
ranges = []

def palindrome(num):
    num_str = str(num)
    rev_str = num_str[::-1]
    if num_str == rev_str:
        return num_str

f = open("C-small-attempt0.in","r")
num = int(f.next())
for ii in range(num):
    line = f.next()
    minimum = int(line.split()[0])
    maximum = int(line.split()[1])
    ranges.append([minimum,maximum])

jj = 0
for element in ranges:
    count = 0
    for ii in range(element[0],element[1]+1):
        sqrt_ii = math.sqrt(ii)
        if sqrt_ii - int(sqrt_ii) == 0.0:
            if not palindrome(ii) is None:
                if not palindrome(int(sqrt_ii)) is None:
                    count += 1
    jj += 1
    print "Case #%d: %d"%(jj,count)

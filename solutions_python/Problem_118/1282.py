#!/usr/bin/env python

import math

def is_palindrome(num):
    num = str(num)
    for i in range(len(num)/2):
        if num[i] != num[len(num)-1-i]:
            return False
    return True

def is_square(num):
    a = long(math.sqrt(num)+0.5)
    return a*a==num


total = int(raw_input())

for case in xrange(1, total+1):
    low, high = map(int, raw_input().split())
    count = 0
    for i in range(low, high+1):
        if not is_palindrome(i):
            continue
        elif not is_square(i):
            continue
        else:
            sqrnum = long(math.sqrt(i))
            if not is_palindrome(sqrnum):
                continue
            else:
                count += 1
    print "Case #%d: %d" % (case, count)

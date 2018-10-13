#!/usr/bin/env python
import sys
import math

def ReverseNumber(n, partial=0):
    if n == 0:
        return partial
    return ReverseNumber(n / 10, partial * 10 + n % 10)

def is_pallindrome(n) :
    return ReverseNumber(n) == n


input = sys.stdin
tc = int(input.readline())
max_n = (10 ** 7) + 5
nice_nos = [1]

for i in xrange(1, max_n + 1):
    last_nice = nice_nos[-1]
    if is_pallindrome(i) and is_pallindrome(i * i):
        nice_nos.append(last_nice + 1)
    else:
        nice_nos.append(last_nice)

no = 0
for line in input:
    no = no +1
    s = line.split()
    a = int(s[0])
    b = int(s[1])
    lower = int(math.ceil(math.sqrt(a)))
    higher = int(math.floor(math.sqrt(b)))
    result = nice_nos[higher] - nice_nos[lower - 1]
    print "Case #%d: %d"%(no, result)


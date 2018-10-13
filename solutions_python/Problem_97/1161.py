#!/usr/bin/env python
import sys
import math

def recycle(x, B):
    num_digits = int(math.log(x, 10))+1
    num = x
    result = set([])
    for i in range(num_digits-1):
        num = (num // 10) + ((num % 10) * (10**(num_digits-1)))
        if num > x and num <= B:
            result.add(num)
    return len(result)

def recycled_count(A, B):
    return sum(recycle(i, B) for i in range(A, B))

with open(sys.argv[1], 'r') as f:
    T = int(f.readline())
    i = 0
    while i < T:
        A, B = map(int,f.readline().split())
        print "Case #%d: %d" % (i+1, recycled_count(A, B))
        i += 1

#!/usr/bin/env python
import sys
import math

def is_palindrome(N):
    num = str(N)
    for i in xrange((len(num) / 2) + 1):
        if num[i] != num[len(num) - (1 + i)]:
            return False
    return True

filename = sys.argv[1]
f = open(filename)
num_cases = int(f.readline().strip())
for case in xrange(num_cases):
    N, M = [int(x) for x in f.readline().strip().split(" ")]
    count = 0
    for i in xrange(int(math.sqrt(N)), int(math.sqrt(M)) + 1):
        sq = i * i
        if is_palindrome(i) and is_palindrome(sq) and sq >= N and sq <= M:
            count += 1
    print "Case #%d: %d" % (case + 1, count)

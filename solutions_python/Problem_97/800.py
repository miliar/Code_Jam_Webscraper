#!/usr/bin/python

import sys

dict = {}

def solve(case):
    count = 0
    A = int(case[0])
    B = int(case[1])
    
    for n in xrange(A, B + 1):
        if not n in dict:
            n_str = str(n)
            dict[n] = dict.fromkeys([int(n_str[i:] + n_str[:i]) for i in xrange(1, len(n_str))]).keys()
        for m in dict[n]:
            if m >= A and m <= B and m > n:
                count += 1
    
    return count

input = [line.strip().split() for line in sys.stdin]

for index in xrange(1, int(input[0][0]) + 1):
    print 'Case #%d: %d' % (index, solve(input[index]))

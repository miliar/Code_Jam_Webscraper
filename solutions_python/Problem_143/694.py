#! python

import sys

## naive attempt, just enumerate them all
def process(A, B, K):
    num = 0
    for a in xrange(A):
        for b in xrange(B):
            if a & b < K:
                num +=1
    return num

with open(sys.argv[1], 'r') as f:
    cases = int(f.readline())
    for case in xrange(cases):
        A, B, K = map(int, f.readline().split())
        print 'Case #%d: %s' % (case+1, process(A, B, K))

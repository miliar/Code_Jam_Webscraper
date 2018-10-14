import sys
import itertools
import copy

sample_count = int(raw_input())
for i in xrange(1, sample_count + 1):
    print 'Case #%d:' % i,
    A, B, K = [int(s) for s in raw_input().split(' ')]
    count = 0
    for comb in itertools.product(xrange(0, A), xrange(0, B)):
        if comb[0] & comb[1] < K:
            count += 1
    print count

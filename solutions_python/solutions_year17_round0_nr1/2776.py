#!/usr/bin/env python

import sys

n_tests = input()
for test_no in xrange(1, n_tests + 1):
    s, k = raw_input().split()
    s = list(s)
    n = len(s)
    k = int(k)
    num_turns = 0
    for i in xrange(n - k + 1):
        #print '{0}{1}'.format(' ' * i, s[i:i+k])
        if s[i] == '-':
            num_turns += 1
            for j in xrange(i, i+k):
                s[j] = '+' if s[j] == '-' else '-'
    #print s, k

    try:
        s.index('-')
        print 'Case #{0}: IMPOSSIBLE'.format(test_no)
    except ValueError:
        print 'Case #{0}: {1}'.format(test_no, num_turns)

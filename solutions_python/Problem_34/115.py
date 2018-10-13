import re, sys

L, D, N = [int(s) for s in raw_input().split()]
words = [raw_input() for _ in xrange(D)]
for i in xrange(N):
    pattern = raw_input().replace('(', '[').replace(')', ']')
    print 'Case #%d: %d' % (i+1, sum(1 for w in words if re.match(pattern, w)))

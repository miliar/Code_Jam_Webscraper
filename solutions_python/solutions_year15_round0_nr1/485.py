#!/usr/bin/env python

for cas in xrange(input()):
    _, S = raw_input().strip().split()
    ans, seen = 0, 0
    for i, s in enumerate(map(int,S)):
        old, ans = ans, ans + max(0, i-seen)
        seen += s + (ans-old)
    print 'Case #%d: %d' % (cas+1, ans)

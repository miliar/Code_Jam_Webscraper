#!/usr/bin/env python

import re
import sys

ldn = re.search(r'(\d+) (\d+) (\d+)', sys.stdin.readline())
L = int(ldn.group(1))
D = int(ldn.group(2))
N = int(ldn.group(3))

words = []    
for i in xrange(0, D):
    words.append(sys.stdin.readline().strip())

for n in xrange(1, N + 1):
    count = 0
    t = sys.stdin.readline().strip()
    t = t.replace('(', '[')
    t = t.replace(')', ']')
    pattern = re.compile(t)
    for w in words:
        if pattern.match(w):
            count += 1
    print "Case #%s: %s" % (n, count)

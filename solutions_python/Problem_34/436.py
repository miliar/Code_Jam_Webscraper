#/usr/bin/env python

import re

f = file('a.in')

L, D, N = map(int, f.readline().split())

words = []
for i in range(D):
    words.append(f.readline().strip())

for i in range(N):
    c = f.readline().strip()
    c = c.replace('(', '[').replace(')', ']')
    r = re.compile(c)
    count = 0
    for word in words:
        if r.match(word):
            count += 1
    print "Case #%d: %d" % (i+1, count)


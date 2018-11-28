#!/usr/bin/env python
import math

p = 'B'
s = 'small-attempt%d' % 0
l = 'large'
current = '%s-%s' % (p, l)

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

t = int(lines[0])

for i in xrange(1, t + 1):
    s = lines[i].split()
    l, p, c = map(int, s)
    n = math.ceil((math.log(float(p) / float(l))) / math.log(c))
    count = math.ceil(math.log(n) / math.log(2))
    print "Case #%d: %d" % (i, count)
    g.write("Case #%d: %d\n" % (i, count))

g.close()

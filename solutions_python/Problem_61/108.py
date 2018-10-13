#!/usr/bin/env python
p = 'C'
s = 'small-attempt%d' % 2
l = 'large'
current = '%s-%s' % (p, s)

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

t = int(lines[0])

def cxy(x, y):
    ret = 1.0
    for i in xrange(y):
        ret *= float(x - i) / float(i + 1)
    return ret

def count(num, pos):
    c = 0
    if pos == 1:
        c += 1
    else:
        for i in xrange(1, min(num - pos, pos - 1) + 1):
            c += cxy(num - pos - 1, i - 1) * count(pos, pos - i)
    return c

for i in xrange(1, t + 1):
    n = int(lines[i])
    c = 1
    for j in xrange(2, n):
        for k in xrange(1, min(n - j, j - 1) + 1):
            print n - j - 1, k - 1, cxy(n - j - 1, k - 1)
            c += cxy(n - j - 1, k - 1) * count(j, j - k)
    c = c % 100003
    print "Case #%d: %d" % (i, c)
    g.write("Case #%d: %d\n" % (i, c))

g.close()

#!/usr/bin/env python

p = 'C'
s = 'small-attempt%d' % 0
l = 'large'
current = '%s-%s' % (p, s)

f = open('%s.in' % current, 'r')
g = open('%s.out' % current, 'w')
lines = f.readlines()
f.close()

def money(r, k, n, l):
    w = 0
    m = 0
    for i in range(0, r):
        t = 0
        g = 0
        while t + l[w] <= k:
            t += l[w]
            g += 1
            w = (w + 1) % n
            if g == n:
                break
        m += t
    return m

case = int(lines[0])
for i in range(1, case + 1):
    a = lines[2 * i - 1].split(' ')
    l = lines[2 * i].split(' ')
    r = int(a[0])
    k = int(a[1])
    n = int(a[2])
    l = [int(x) for x in l]
    m = money(r, k, n, l)
    #print 'Case #%d: %d\n' % (i, m)
    g.write('Case #%d: %d\n' % (i, m))

g.close()

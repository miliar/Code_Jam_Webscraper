#!/usr/bin/env python

m = {}
s = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv'
s2 = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up'

for i,j in zip(s,s2):
    m[i] = j

m['z'] = 'q'
m['q'] = 'z'

f = open('A-small-attempt0.in')
out = open('outputS.txt', 'w')

t = int(f.readline())

for i in range(t):
    g = f.readline()
    s = ''
    for j in g[:-1]:
        s += m[j]
    out.write('Case #%d: %s\n' % (i + 1, s))

#!/usr/bin/python

trans = {}

def solve():
    line = raw_input()
    res = ''
    for c in line:
        res = res + trans.get(c, c)
    print res

def populate():
    hints = [
        ('our language is impossible to understand', 'ejp mysljylc kd kxveddknmc re jsicpdrysi'),
        ('there are twenty six factorial possibilities', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'),
        ('so it is okay if you want to just give up', 'de kr kd eoya kw aej tysr re ujdr lkgc jv'),
        ('a zoo', 'y qee'),
        ('q', 'z'),
    ]

    for h in hints:
        a, b = h
        n = len(a)
        assert len(a) == len(b)
        for i in xrange(n):
            trans[b[i]] = a[i]

populate()

nt = int(raw_input())
for _ in xrange(nt):
    print 'Case #%d:' % (_+1),
    solve()

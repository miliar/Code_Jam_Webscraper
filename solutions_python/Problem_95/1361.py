#!/usr/bin/python

encoded = (
        'ejp mysljylc kd kxveddknmc re jsicpdrysi',
        'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd',
        'de kr kd eoya kw aej tysr re ujdr lkgc jv'
        )

plain = (
        'our language is impossible to understand',
        'there are twenty six factorial possibilities',
        'so it is okay if you want to just give up',
        )

mapping = {'y':'a', 'e':'o', 'q':'z'}

se, sp = set("bcdfghijklmnoprstuvwxyz"), set("bcdefghijklmnpqrstuvwxy")
for x in xrange(3):
    e, p = encoded[x], plain[x]
    for y in xrange(len(e)):
        a, b = e[y], p[y]
        if a in se: se.remove(a)
        if b in sp: sp.remove(b)
        mapping[e[y]] = p[y]

#print se, sp
if len(se) == 1:
    se = tuple(se)
    sp = tuple(sp)
    mapping[se[0]] = sp[0]
#print sorted(mapping.keys())

t = input()
for x in xrange(t):
    msg = raw_input().strip()
    print 'Case #%d: %s' % (x+1, ''.join(mapping[x] for x in msg))

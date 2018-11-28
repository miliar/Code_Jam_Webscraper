#!/usr/bin/python
inf = open('in', 'r')
outf = open('out', 'w')

translation = {}
strs = ['ejp mysljylc kd kxveddknmc re jsicpdrysi', 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd', 'de kr kd eoya kw aej tysr re ujdr lkgc jv']
answ = ['our language is impossible to understand', 'there are twenty six factorial possibilities', 'so it is okay if you want to just give up']

mapping = dict()
j = 0
for strr in strs:
    i = 0
    for char in strr:
        mapping[char] = answ[j][i]
        i += 1
    j += 1

i = 1
strings = inf.read().split("\n")
mapping['q'] = 'z'
mapping['z'] = 'q'
for strr in strings[1:]:
    if not len(strr):
        continue
    out = ''
    for char in strr:
        out += mapping[char]
    print "Case #%d: %s" % (i, out)
    i += 1

inf.close()
outf.close()

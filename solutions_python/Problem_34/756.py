#!/usr/bin/env python
import re
import operator

regexp = re.compile('(\([a-z]+\)|[a-z])')
inf = open('./A-large.in','r')
file = inf.readlines()

file = map(lambda x: x[:-1], file)
(L,D,N) = map(int, file[0].split(' '))

lang = file[1:D+1]

patterns = map(lambda x: filter(lambda y: y!='', x), map(regexp.split, file[D+1:]))

for i in xrange(len(patterns)):
    matches = 0
    for w in lang:
        fail = 0
        for j in xrange(len(w)):
            if not (w[j] in patterns[i][j]):
                fail = 1

        if not fail:
            matches = matches + 1
    print("Case #{0}: {1}".format(i+1, matches))

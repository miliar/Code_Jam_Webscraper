#!/usr/bin/env python

# Google Code Jam
# Qualification Round
# Problem A
# Saving the Universe
#
# Yatsenko Mikhail


from sys import stdin
from sets import Set

lst = stdin.read()
lst = lst.split('\n')

N = int(lst[0])
inc = 1
for case in xrange(N):
    S = int(lst[inc])
    inc += 1
    searchEngines = lst[inc:inc + S]

    inc += S
    Q = int(lst[inc])
    inc += 1
    queries = lst[inc:inc + Q]
    inc += Q

#    print S
#    print searchEngines
#    print Q
#    print queries

    uniq = Set()
    count = 0
    for x in queries:
        uniq.add(x)
        if len(uniq) == S: 
            uniq = Set([x])
            count += 1
    
    print 'Case #%d: %d' % (case + 1, count)

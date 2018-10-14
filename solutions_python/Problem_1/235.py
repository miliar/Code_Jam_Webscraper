#!/usr/bin/python

from sol import *

c = next_int()

for x in range(1,c+1):

    s = next_int()
    engines = [ next_line() for i in range(s) ]

    res = 0

    q = next_int()
    used = []
    for i in range(q):
        query = next_line()
        if query not in used:
            used.append( query )
            if len(used) == s:
                res += 1
                used = [query]

    print 'Case #%d: %d' % (x, res)

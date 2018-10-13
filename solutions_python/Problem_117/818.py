#!/usr/bin/env python
#
# Luke Southam <luke@devthe.com>
# GCJ Problem B. Lawnmower
#


lenr = lambda *args, **kwargs: xrange(len(*args, **kwargs))

T = int(raw_input())

for test_i in xrange(T):
    N, M = map(int, raw_input().split())
    pattern = [map(int, raw_input().split()) for i in xrange(N)]

    possible = "YES" # Lets be optimistic.

    columns = [[pattern[y][x] for y in lenr(pattern)] for x in lenr(pattern[0])]
    

    row_max = map(max, pattern)
    column_max = map(max, columns)
    
    for y in lenr(pattern):
        for x in lenr(pattern[y]):
            if pattern[y][x] != row_max[y] and pattern[y][x] != column_max[x]:
                possible = "NO" # Oh well.
                    
    print "Case #%i: %s" % (test_i + 1, possible)


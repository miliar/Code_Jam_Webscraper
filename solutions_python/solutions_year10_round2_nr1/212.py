#!/usr/bin/env python

import fileinput

inp = fileinput.input()

t = int(inp.readline())

def proc_dir(di, exists):
    if di in exists:
        return 0
    else:
         parent_cost = proc_dir(di[:di.rindex('/')], exists)
         exists.add(di)
         return 1 + parent_cost

def go():
    n, m = map(int, inp.readline().split())
    # already existing
    exists = set()
    exists.add('')
    for i in xrange(n):
        di = inp.readline().strip()
        if di[-1] == '/':
            di = di[:-1] 
        exists.add(di)

    ccount = 0  
    # to create
    for i in xrange(m):
        di = inp.readline().strip()
        if di[-1] == '/':
            di = di[:-1]
        ccount += proc_dir(di, exists)

    return ccount

for i in xrange(t):
    print 'Case #%d: %d' % (i+1, go())

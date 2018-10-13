#!/usr/bin/env python
from itertools import count

transtab = { '1': { '1':'1', 'i':'i', 'j':'j', 'k':'k'},
          'i': { '1':'i', 'i':'-1', 'j':'k', 'k':'-j'},
          'j': { '1':'j', 'i':'-k', 'j':'-1', 'k':'i'},
          'k': { '1':'k', 'i':'j', 'j':'-i', 'k':'-1'} }

def trans(a,b):
    if len(a)>1:
        v = transtab[a[1]][b]
        if len(v)>1:
            return v[1]
        else:
            return '-' + v
    else:
        return transtab[a][b]

def solve(ijk):
    first = '1'
    for i, c in enumerate(ijk):
        first = trans(first,c)
        if first=='i': break
    if i>=len(ijk)-2: return 'NO'
    second = '1'
    for j in xrange(i+1,len(ijk)):
        c = ijk[j]
        second = trans(second,c)
        if second=='j': break
    if j>=len(ijk)-1: return 'NO'
    third = '1'
    for k in xrange(j+1,len(ijk)):
        c = ijk[k]
        third = trans(third,c)
    if first=='i' and second=='j' and third=='k':
        return 'YES'
    else:
        return 'NO'

for cas in xrange(input()):
    L, X = map(int, raw_input().strip().split())
    ijk = raw_input()*X
    print "Case #%d: %s" % (cas+1, solve(ijk))

#!/usr/bin/python

import sys
import math
import copy

f = open(sys.argv[1],'r')

num = int(f.readline())


def open_chest(o,k,c):
    #print o, k
    #if len(o) == 4:
        #print o,k
    if len(o) == len(c):
        return o
    if open_chest.cache.has_key(tuple(sorted(o))):
        return open_chest.cache[tuple(sorted((o)))]
    for i in xrange(len(c)):
        if i in o:
            continue
        if c[i][0] not in k:
            continue
        on = o + (i,)
        kind = k.index(c[i][0])
        kn = k[:kind] + k[kind+1:] + c[i][1]
        oc = open_chest(on, kn, c)
        open_chest.cache[tuple(sorted(on))] = oc
        if oc:
            return oc
    return []

for i in range(num):
    open_chest.cache = {}
    line = f.readline()
    k,n = line.split()
    k = int(k)
    n = int(n)
    line = f.readline()
    keys = tuple([int(x) for x in line.split()])
    chest = []
    for j in range(n):
        line = f.readline()
        line = [int(x) for x in line.split()]
        chest.append((line[0], tuple(line[2:])))
    o = ()
    #print k,n,keys,chest
    #print open_chest(o,keys, chest)
    oc =  open_chest(o,keys, chest)
    if oc:
        oc = [str(x+1) for x in oc]
        oc = ' '.join(oc)
        print 'Case #{}:'.format(i+1), oc
    else:
        print 'Case #{}: IMPOSSIBLE'.format(i+1)

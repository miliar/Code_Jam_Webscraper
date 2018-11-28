# -*- coding: utf-8 -*-
import sys
import itertools

def all_perm(lists):
    return [ "".join(i) for i in itertools.permutations( lists )]


f = open(sys.argv[1], 'r')
line = f.readline().strip()


for i in range( int(line) ):
    res = {}
    a, b = f.readline().strip().split()
    ia = int(a)
    ib = int(b)
    for j in range( ia, ib+1 ):
        for k in all_perm( str(j) ):
            if j < int(k) and int(k)<=ib :
                res[ str(j)+':'+k ] = 1

    count = 0
    for j in res:
        n, m = j.split(':')
        flag = False
        for idx, val in enumerate(n):
            tt = n[idx:]+ n[0:idx]
            if tt == m:
                flag = True
        if flag==True:
            count += 1
    print "Case #%d: %d" % ( i+1, count)

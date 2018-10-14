# -* coding:utf-8 -*-
#! /usr/bin/python

import sys
import math
import numpy

input=sys.stdin.read()
inList=input.split('\n')
N=int(inList.pop(0))



def permutation(seq):
    if len(seq) == 1:
        yield seq
    for i in range(len(seq)):
        for j in permutation(seq[:i] + seq[i+1:]):
            yield seq[i:i+1] + j 


def rl( s ):
    ret = 1
    cur = s[0]
    for i in s[1:]:
        if cur != i:
            ret+= 1
            cur = i
    return ret

def f(s,k):
    a = range(k)

    n = len(s)/k
    b = []
    for i in range(n):
        b.append( s[i*k:i*k+k])

    r = 100000000
    for d in  permutation(a):
        s2 = ""
        for j in range(n):
            for i in d:
                s2 += b[j][i]
        tmp = rl( s2 )
        if tmp < r:
            r = tmp
    return r

for i in range(N):
    k = int(inList.pop(0))
    s = inList.pop(0)
    res = f( s,k )

    print "Case #%d: %d"%(i+1, res)


    

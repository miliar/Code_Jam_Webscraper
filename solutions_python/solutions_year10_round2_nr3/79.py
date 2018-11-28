#!/usr/bin/env python
#By Jai Dhyani

import math, sys, os
from scipy.misc import comb

cache = { 0: {0:0,1:0}, 1: {1:0,0:0}, 2: {1:1} }

def getints(f):
    return [int(x) for x in f.readline().split()]

def solve_nk(n,k):
    if n<=1:
        return 0
    if  k in (1,2):
        return 1
    if n in cache and k in cache[n]:
        return cache[n][k]
    else:
        if not n in cache:
            cache[n] = dict()
        cache[n][k] = sum( [solve_nk(k,i)*comb(n-k-1,k-i-1,exact=1) for i in
                            xrange(1,k) ] )
        print n,k,cache[n][k]
        return cache[n][k]


def solve( x ):
    n = x[0]
    return sum( solve_nk(n,k) for k in range(1,n) )

if __name__ == '__main__':
    filenames = [f for f in os.listdir('.') if f[-2:]=='in']
    for filename in filenames:
        outname=filename+'.out'
        f=open(filename)
        out=open(outname,'w')
        try:
            numtrials = getints(f)[0]
        except IndexError as ie:
            print 'no input data in %s'%filename
            exit(0)
        for i in xrange(numtrials):
            answer_num = solve(getints(f))%100003
            answer_str = "Case #%d: %d"%(i+1,answer_num)
            print(answer_str)
            out.write(answer_str+'\n')

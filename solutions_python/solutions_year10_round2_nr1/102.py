#!/usr/bin/env python
#By Jai Dhyani

import math, sys, os

def getints(f):
    return [int(x) for x in f.readline().split()]

def solve( f ):
    dirs_existing = dict()
    dirs_wanted = dict()
    n_fexist, n_fcreat = getints(f)
    for i in xrange(n_fexist):
        path=f.readline()[:-1]
        parts=path.split('/')
        x = dirs_existing
        for p in parts[1:]:
            if not p in x:
                x[p] =dict()
            x = x[p]
    mkdir_count=0
    for i in xrange(n_fcreat):
        path=f.readline()[:-1]
        parts=path.split('/')
        x = dirs_existing
        for p in parts[1:]:
            if not p in x:
                x[p]=dict()
                mkdir_count +=1
            x = x[p]
    return mkdir_count

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
            answer_num = solve(f)
            answer_str = "Case #%d: %d"%(i+1,answer_num)
            print(answer_str)
            out.write(answer_str+'\n')

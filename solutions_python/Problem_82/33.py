#!/usr/bin/python

__author__ = "Thomas van den Berg"

# from itertools import izip, permutations
# from numpy import *
from pprint import pprint

def avg(l):
    return sum(l)/float(len(l))

fn = 'B-large.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    
    (C,D) = [int(d) for d in f.readline().split()]
    
    blocks = []
    vtotal = 0
    for i in xrange(C):
        (P,V) = [int(d) for d in f.readline().split()]
        t = (D*(V-1))/2.0
        vtotal += V
        left = P - t
        right = P + t
        blocks.append( (left, right, t) )
        
    shifted = True
    # print "CASE %d, %d"%(D,vtotal)
    while shifted:
        blocks = sorted(blocks, key = lambda x: (x[0]+x[1])/2.0)
        shifted = False
        for i in xrange(len(blocks)-1):
            (left1,right1,t1),(left2,right2,t2) = blocks[i],blocks[i+1]
            dist = left2-right1
            s = (D - dist)
            if s > 0:
                td = t2-t1
                s1 = min(s,max(0,(s + td)/2.0))
                s2 = min(s,max(0,(s - td)/2.0))
                nb = (left1-s1, right2+s2, max(t1+s1,t2+s2))
                # print "Merged:  %s and %s  --> %s\nwith s=%g, td=%g, s1=%g, s2=%g" %(blocks[i], blocks[i+1],nb,s,td,s1,s2)
                blocks = blocks[:i] + [nb] + blocks[i+2:]
                shifted = True
                break
        # pprint(blocks)
        
    
    ts = (b[2] for b in blocks)
    ans = max(ts)
    # print 'ANS', ans
    fout.write('Case #%d: %s\n'%(case+1,ans))
    

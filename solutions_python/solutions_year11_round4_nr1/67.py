#!/usr/bin/python

__author__ = "Thomas van den Berg"

# from itertools import izip, permutations
# from numpy import *
from pprint import pprint

def avg(l):
    return sum(l)/float(len(l))

fn = 'A-large.in'
f = open(fn,'r')
fout = open(fn.replace('.in','.out'),'w')

T = int(f.readline())
for case in xrange(T):
    (X,S,R,t,N) = [int(d) for d in f.readline().split()]
    
    print X,S,R,t,N
    last = 0
    intervals = []
    for n in xrange(N):
        B,E,w = [int(d) for d in f.readline().split()]
        if B > last:
            intv = [last, B, S]
            intervals.append(intv)
        intervals.append([B,E,S+w])
        last = E
    if last < X:
        intervals.append([last,X,S])

    ran = []
    while t > 0 and intervals:
        intervals.sort(key=lambda x:x[2])
        intv = intervals[0]
        d = intv[1] - intv[0]
        w = float(intv[2] + (R-S))
        rt = d/w
        if t >= rt:
            intv[2] += (R-S) # Running speed
            ran.append(intv)
            intervals = intervals[1:]
            t -= rt
        else:
            newintv = [intv[0],intv[0]+(t*w),intv[2]+R-S]
            ran.append(newintv)
            intv[0] += t*w
            t = 0
    
    allintv = sorted(intervals+ran)

    total = 0.0
    for (bg,en,sp) in allintv:
        tm = (en-bg)/float(sp)
        total += tm
        
    ans = total
    print ans
    fout.write('Case #%d: %s\n'%(case+1,ans))
    

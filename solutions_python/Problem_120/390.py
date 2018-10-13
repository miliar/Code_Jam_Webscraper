#!/usr/bin/env python

data=[i*i for i in xrange(0,1000)]

t=int(raw_input())

for i in xrange(0,t):
    s=raw_input()
    (r,t)=[int(k) for k in s.split(' ')]
    sum=0
    ring=0
    for j in xrange(r,1000,2):
        sum+=data[j+1]-data[j]
        ring+=1
        if sum>t:
            ring-=1
            break
    print('Case #%d: %d' % (i+1, ring,))
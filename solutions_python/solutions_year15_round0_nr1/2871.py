#!/usr/bin/env python
 
import sys
 
f=open(sys.argv[1],"r")
T=int(f.readline())
 
for i in range(1,T+1):
    smax,a=f.readline().split()   
    smax=int(smax)
    a=map(int,a)
    #print "case",i,smax,a
    sum=0
    friends=0
    for j in range(smax+1):
        #print "loop",j,sum,friends
        if (sum+friends<j):
            friends+=j-(sum+friends)
        sum+=a[j]
    #print "results", i,friends
    print "Case #%i: %i" % (i, friends)
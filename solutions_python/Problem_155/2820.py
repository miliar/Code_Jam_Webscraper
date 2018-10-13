#!/usr/bin/python

# Yun Liu liuyun@mit.edu / liuyun86@gmail.com
# usage: python run.py A-small-attempt0.in > A-small-attempt0.out

import sys

f=open(sys.argv[1])

n=int(f.readline())

for i in range(n):
    line=f.readline().strip().split()
    s_max=int(line[0])
    vals=line[1]
    #print('\n\n%d %s'%(s_max,vals))

    x=-1 # current shyness
    cum_count=0 # n standing now
    n_needed=0
    for v in vals:
        x+=1
        diff=0
        if cum_count<x:
            diff=x-cum_count
            n_needed+=diff
        cum_count+=int(v)+diff
        #print('%d %s %d %d'%(x,v,cum_count,n_needed))
    print('Case #%d: %d'%(i+1,n_needed))
        
        


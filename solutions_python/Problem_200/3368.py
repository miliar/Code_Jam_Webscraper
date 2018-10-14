import sys
import math

t = int(raw_input())  # read a line with a single integer
for jj in xrange(1, t+1):
#for jj in xrange(1, 6):
    
    a=[]
    a = [int(s) for s in raw_input()]
    #print a
    i = 1
    sm = len(a)
    backwds = False
    while i<len(a) and i>0:
        if a[i]<a[i-1]:
            a[i-1]-=1
            sm=i-1
            i=i-1
            backwds = True
        elif not backwds:
            i = i+1
        elif backwds:
            break
                                    
    #print sm, len(a), a
    for i in xrange(sm+1,len(a)):
        a[i]=9
    
    N = int(''.join([str(q) for q in a]))
    
    print "Case #{}: {}".format(jj, N)


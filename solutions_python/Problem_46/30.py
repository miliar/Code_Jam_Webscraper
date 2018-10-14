import sys
import math

T = int(raw_input())

for c in xrange(1,T+1):
    N = int(raw_input())
    x = []
    for i in xrange(0,N):
        arr = list(raw_input())
        k=-1
        for j in xrange(0,N):
            if arr[j] == '1':
                k = j
        x.append(k)
    
    
    count=0
    for i in xrange(0,N):
        if (x[i]>i):
            for j in xrange(i+1,N):
                if x[j]<=i:
                    break;            
            count+=j-i
            tmp = x[j]
            k=j
            while(k>i):
                x[k]=x[k-1]
                k-=1
            x[i]=tmp
    print "Case #%d: %d"%(c,count)
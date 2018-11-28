f = open('A-large.in', 'r')

T = int(f.readline().strip())

import math

for t in xrange(T):

    N = int(f.readline().strip())        
    m = [int(x) for x in f.readline().strip().split()]

    i=0
    s1=0
    ms=0
    while i<len(m):

        if i+1<len(m):
            if m[i]-m[i+1]>0:
                s1+=m[i]-m[i+1]
                if m[i]-m[i+1]>ms:
                    ms=m[i]-m[i+1]
        i+=1

    i=0
    s2=0
    while i<len(m)-1:

        if m[i]<ms:
            s2+=m[i]
        else:
            s2+=ms
        i+=1


    print 'Case #%d: %d %d'% (t+1,s1,s2)




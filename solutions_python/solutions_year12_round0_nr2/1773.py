#!/usr/bin/env python2
# we use tr ' ' ',' to pass input to the script on a unix system

N=input()

for n in xrange(1,N+1):
    max=0
    L=input()
    S=L[1]
    p=L[2]
    for l in L[3:]:
        if (l+2)/3 >= p :
           max = max + 1
        elif ((S>0) and ((l+1)/3 > p-2) and l>1):
           max = max + 1
           S = S - 1
    print "Case #%d: %d" % (n, max)

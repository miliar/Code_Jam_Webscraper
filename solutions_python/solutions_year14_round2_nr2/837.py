#!/usr/bin/env python

f = open('B-small-attempt1.in','r')

T = int(f.readline().rstrip('\n'))

for x in range(1,T+1):
    L = f.readline().rstrip('\n').split(' ')
    A = int(L[0])
    B = int(L[1])
    K = int(L[2])
    aa = 0
    count = 0
    while aa < A:
        bb = 0
        while bb < B:
            if aa & bb < K:
                count += 1
            bb += 1
        aa += 1
    print "Case #{0}: {1}".format(x,count)
    

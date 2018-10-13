#!/usr/bin/python

T=int(raw_input())
for i in xrange(0,T):
    line=raw_input().split(' ')
    N = int(line[0])
    K = int(line[1])

    domains = 1
    to_place = K
    while(to_place>domains):
        to_place = to_place - domains
        domains = domains * 2

    size_1 = (N-K+to_place)/domains
    size_2 = (N-K+to_place)/domains
    if ((N-K+to_place)%domains):
        size_2 = size_2+1

    if(to_place <= (N-K+to_place)%domains):
        m = min((size_2-1)/2,(size_2-1)/2+(size_2-1)%2)
        M = max((size_2-1)/2,(size_2-1)/2+(size_2-1)%2)
    else:
        m = min((size_1-1)/2,(size_1-1)/2+(size_1-1)%2)
        M = max((size_1-1)/2,(size_1-1)/2+(size_1-1)%2)
    

    print("Case #"+repr(i+1)+": "+repr(M)+" "+repr(m))

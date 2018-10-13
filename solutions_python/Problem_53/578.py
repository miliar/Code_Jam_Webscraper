#!/usr/bin/env python
# -*- coding: ascii -*-

import  math

T = int(raw_input())
for tc in range(T):
    N,K = [int(nk) for nk in raw_input().split()]
    pown = int(math.pow( 2, N ))
    f = K % pown
    if f != pown-1 :
        print "Case #"+str(tc+1)+": OFF"
    else :
        print "Case #"+str(tc+1)+": ON"

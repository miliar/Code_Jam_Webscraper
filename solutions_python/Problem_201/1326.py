#!/usr/bin/env python3
import math

T = int(input())

for t in range(1, T+1):
    N, K = input().split()
    N = int(N)
    K = int(K)
    #print("K : {0} N : {1}".format(K, N))
    n = int(math.log(K, 2))
    a = 2**n
    k = K-a
    chunk_size = int((N-k)/(a))
    #print("k = {0}, n = {1}, chunk_size = {2}".format(k, n, chunk_size))
    #print("async border : {0}".format(async_border))
    print("Case #{0}: {1} {2}".format(t, math.ceil((chunk_size-1)/2), math.floor((chunk_size-1)/2)))

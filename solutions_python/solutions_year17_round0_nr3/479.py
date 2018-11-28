#coding:utf-8

import numpy as np

def p3(N,K):
    a = int(np.log2(K+1))
    if 2**a == K+1:
        a-=1
    k = 2**a - 1
    n = N - k
    step = n//(2**a)
    r = n%(2**a)
    R = K-k    
    
    if R<=r:
        res = step+1
    else:
        res = step
        
    return res-1-(res-1)//2,(res-1)//2


T = int(input())
for t in range(T):
	N,K = input().split()
	N,K = int(N),int(K)
	print( "Case #%d: %d %d"%( t+1,*p3(N,K) ) )

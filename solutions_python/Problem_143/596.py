# -*- coding: utf-8 -*-
"""
Created on Sat May 03 17:12:02 2014

@author: Ennassiri
"""
import numpy as np

f = open( "test1.in", "r" )
out = open( "test1.out", "w")
N = int(f.readline())

result = np.zeros(1001)
def result(A,B,K):
    count = 0
    for i in range(A):
        for j in range(B):
            if i&j < K:
                count += 1
    return count

for n in xrange(1,N+1):
    info = f.readline().strip().split()
    out.write("Case #%d: %d\n" % (n, result(int(info[0]),int(info[1]),int(info[2]))))

f.close()
out.close()
from sys import stdin
from math import *

T = int(stdin.readline())

for t in xrange(0,T):
    N = int(stdin.readline())
    A = []
    B = []
    for i in xrange(0,N):
        nums = stdin.readline()
        nums = nums.split()
        A.append(int(nums[0]))
        B.append(int(nums[1]))
        
    count = 0
    
    for i in xrange(0,N):
        for j in xrange(0,N):
            if i==j: continue
            if A[i] > A[j] and B[i] < B[j]:
                count+=1

    print "Case #"+str(t+1)+":",count
    
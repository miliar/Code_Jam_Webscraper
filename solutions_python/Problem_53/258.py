from sys import stdin
from math import *

T = int(stdin.readline())

for i in xrange(0,T):
    line = stdin.readline()
    nums = line.split()
    N = int(nums[0])
    K = int(nums[1])
    
    N2 = 2**N
    if (K%N2)==N2-1:
        print "Case #"+str(i+1)+": ON"
    else:
        print "Case #"+str(i+1)+": OFF"
    
    

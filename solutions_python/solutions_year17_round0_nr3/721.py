#!/usr/bin/python
import sys, math        

def maxmin(n, k):
    if n == k:
        return (0, 0)
    right = n / 2 #bigger side
    left = (n-1) / 2 #smaller side
    while k > 1:
        if k % 2 == 0:
            n = right
        else:
            n = left
        k /= 2
        right = n / 2 #bigger side
        left = (n-1) / 2 #smaller side

    return (right, left)
    
    

T = int(sys.stdin.readline())
for t in range(T):
    n, k = map(int, sys.stdin.readline().strip().split(" "))
    (right, left) = maxmin(n, k)
        
    print "Case #%d: %d %d" % ((t + 1), right, left)

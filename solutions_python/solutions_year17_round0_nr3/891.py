#!/usr/bin/env python 
import math
def solve(N,K):
    K=int(K)
    N=int(N)
    h=math.floor(math.log(K,2))+1
    nodesInLevel=int(2**(h-1))
    placedTillLevel=nodesInLevel-1
    indexInLevel = K-placedTillLevel-1
    lowNodeValue = (N-placedTillLevel) / nodesInLevel
    numberOfLargerNodes = (N-placedTillLevel) % nodesInLevel
    blockSize = lowNodeValue +1 if indexInLevel < numberOfLargerNodes else lowNodeValue 
    return  [blockSize/2,blockSize/2-1] if blockSize % 2 == 0 and blockSize is not 0 else [blockSize/2,blockSize/2]
    
if __name__ == "__main__":
    t = int(raw_input())
    for cas in xrange(1,t+1):
        ans = solve(*raw_input().split())
        print "Case #{}: {} {}".format(cas,ans[0],ans[1])

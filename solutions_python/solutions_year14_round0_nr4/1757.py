import itertools
import multiprocessing 
import sys
import math

def main():    
    tcs = int(sys.stdin.readline())
    for i in range(1, tcs+1):
        l = int(sys.stdin.readline())
        N = [float(x) for x in sys.stdin.readline().split()]
        K = [float(x) for x in sys.stdin.readline().split()]
        N = sorted(N)
        K = sorted(K)
#        print N
#        print list(reversed(K))
        ndw = playDWar(N, K)
        nw = playWar(N, K)
        print "Case #" + str(i) + ": " + str(ndw) + " " + str(nw)

def playWar(N, K):    
    K = list(K)
    nScore = 0
    for n in N:
        flag = 0
        for i in range(0, len(K)):
            if K[i] > n:
                flag = 1
                del K[i]
                break
        if flag == 0:
            nScore += 1
    return nScore
                
            
    return 0

def playDWar(N, K):
    N = list(N)
    nScore = 0
    for k in K:
        flag = 0
        for i in range(0, len(N)):
            if N[i] > k:
                flag = 1
                del N[i]
                break
        if flag == 1:
            nScore += 1
    return nScore


if  __name__ =='__main__':main()

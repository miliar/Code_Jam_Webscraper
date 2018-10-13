import numpy as np
import sys

def readData():
    line = map(int, sys.stdin.readline().split())
    #print "line:", line
    return line[0], line[1]
    


def solve(N, K):
    #print "solve", N, K
    if N == K:
        return 0, 0
    n, k = N-1, 0
    #print N, K
    left, right = n/2 + (n % 2),  n/2
    while (K - k) > 1:
        k += 1
        if (K-k) % 2 == 1:
            n = left
            k += (K-k)/2
            #print "left", k
        else:
            n = right
            k += (K-k)/2
            #print "right", k
        n -= 1
        left, right = n/2 + (n % 2),  n/2
    #l, r
    return (left, right)
            
    



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    result = 0
    for t in xrange(T):
        data = readData()
        result = solve(*data)
        sys.stdout.write("Case #%d:" % (t+1))
        for i in xrange(len(result)):
            sys.stdout.write(" %d" % result[i])
        sys.stdout.write("\n")
        
        

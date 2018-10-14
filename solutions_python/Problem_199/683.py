import numpy as np
import sys

def readData():
    line = sys.stdin.readline().split()
    K = int(line[-1])
    line = np.fromstring(line[0], dtype=np.uint8)
    #print "line:", line
    inp = np.where(line == 43, 1, 0).astype(bool) #45 represents -, 43 represents +
    return inp, K
    


def solve(pancakes, K):
    #print "pancakes:", pancakes
    #print "K:", K
    n = len(pancakes)
    zeros = n - pancakes.sum()
    #print "zeros:", zeros
    
    if zeros == 0:
        return 0
    if K == 1:
        return zeros
    
    nflips = 0
    
    i = 0
    istop = n-K+1
    while i < istop:
        if not pancakes[i]:
            pcks = pancakes[i:i+K]
            #zeros = zeros + pcks.sum() - (K-pcks.sum())
            #nones =  
            zeros = zeros - K + 2 * pcks.sum()
            pancakes[i:i+K] = ~pcks
            nflips += 1
        #print i, pancakes, zeros, nflips
        i += 1
            
    return nflips if zeros == 0 else "IMPOSSIBLE"
            
    



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    result = 0
    for t in xrange(T):
        data = readData()
        result = solve(*data)
        print "Case #"+str(t+1)+":",result
        

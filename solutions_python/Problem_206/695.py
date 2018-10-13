import numpy as np
import sys

def readData():
    line = sys.stdin.readline().split()
    D, N = map(int, line)
    
    horses = np.empty((N,2), dtype=int)
    for i in xrange(N):
        horses[i] = map(int, sys.stdin.readline().split())
    
    ix = np.argsort(horses[:,0])
    horses = horses[ix]
        
    return D, N, horses


def solve(D, N, horses):
    #print D, N, horses
    
    time = (1.*D-horses[:,0])/horses[:,1]
    #print "time:", time
    maxtime = np.amax(time)
    
    
    return D/maxtime
    



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    result = 0
    for t in xrange(T):
        data = readData()
        result = solve(*data)
        print("Case #%d: %.6f" % ((t+1), result))
              

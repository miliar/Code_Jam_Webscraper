import numpy as np
import sys

def readData():
    line = sys.stdin.readline()
    line = np.fromstring(line[:-1], dtype=np.uint8) - 48
    #print "line:", line
    return line
    


def solve(N):
    if len(N) == 1:
        return N
    #sz = N if N[-1] != 0 and N[-1] >= N[-2] else N-1
    sz = len(N)
    R = np.zeros(sz, dtype=int)
    #decr = False
    lastflip = sz
    
    for i in xrange(sz-1, 0, -1):
        if(N[i] != 0 and N[i] >= N[i-1]):
            R[i] = N[i] 
        else:
            #print "flip all"
            R[i:lastflip] = 9
            lastflip = i
            
            
            j = i-1
            while j >= 0 and N[j] == 0:
                N[j] = 9
                j -= 1
            N[j] -= 1
        #print "N, R:", N, R
    R[0] = N[0]
    return R if R[0] > 0 else R[1:]
            
    



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    result = 0
    for t in xrange(T):
        data = readData()
        result = solve(data)
        sys.stdout.write("Case #%d: " % (t+1))
        for i in xrange(len(result)):
            sys.stdout.write("%d" % result[i])
        sys.stdout.write("\n")
        
        

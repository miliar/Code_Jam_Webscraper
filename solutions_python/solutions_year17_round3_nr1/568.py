import numpy as np
import sys, math

def readData():
    N, K = map(int, sys.stdin.readline().split())
    #print "N, K", N, K
    pcks = np.empty((N, 2), dtype=int)
    for i in xrange(N):
        r, h = map(int, sys.stdin.readline().split())
        pcks[i] = [r, h]
    #print pcks
    return N, K, pcks

def solve(N, K, pcks):
    surface = np.empty((N,2))
    surface[:,1] = 2 * math.pi * pcks.prod(axis=1)
    surface[:,0] = pcks[:,0] #r
    #print "surface:", surface
    #ix = np.argsort(surface)[::-1][:K]
    ix = np.lexsort(np.rot90(surface))[::-1]#[:K]
    #print "ix:", ix
    surface = surface[ix]
    #print "surface:", surface

    #hr = np.argmax(pcks[ix,0])
    top = math.pi * surface[:, 0] * surface[:, 0]
    #print "top:", top
    surftop = surface[:,1] + top
    #print "surftop:", surftop

    if K == 1:
        return surftop.max()
    if K == N:
        return surftop[0] + surface[1:,1].sum()

    maxv = -1
    for i in xrange(N-K+1):
        #print "i:", i, surface[i+1:,1]
        ix = np.argsort(surface[i+1:,1])[::-1][:K-1]
        #print "ix:", ix
        s = surface[i+1:,1][ix].sum()

        #surface[i+1:i+K+1,1].sum()
        #print "s:", s, surftop[i], s + surftop[i]
        if surftop[i] + s > maxv:
            maxv = surftop[i] + s
    
    return maxv



if __name__ == "__main__":
    T = int(sys.stdin.readline())
    for t in xrange(T):
        data = readData()
        result = solve(*data)
        print("Case #%d: %.9f" % ((t+1), result))
        

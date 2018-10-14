#Joe Snider
#4/16
#
#code jam 2017, qual C

import numpy as np

#slow as hell, but good for testing
def bruteLs(stalls):
    Ls = [0 for x in stalls]
    for i in xrange(len(stalls)):
        if stalls[i] == 0:
            for j in xrange(1, i+1):
                if stalls[i-j] == 1:
                    Ls[i] = j-1
                    break
    return Ls
def bruteRs(stalls):
    Rs = [0 for x in stalls]
    for i in xrange(len(stalls)):
        if stalls[i] == 0:
            for j in xrange(1, len(stalls)-i):
                if stalls[i+j] == 1:
                    Rs[i] = j-1
                    break
    return Rs

def placeBF(stalls):
    Ls = np.array(bruteLs(stalls))
    Rs = np.array(bruteRs(stalls))
    #print Ls,Rs,
    neighbor = np.minimum(Ls, Rs)
    #print neighbor,
    
    maxmin = np.max(neighbor)

    maxminI = np.nonzero(neighbor >= maxmin)[0]
    avoid = np.maximum(Ls[maxminI], Rs[maxminI])
    #print avoid
    maxmax = np.max(avoid)
    
    maxmaxI = np.nonzero(avoid >= maxmax)[0]

    #print "gh1", maxminI
    #print "gh2", maxmaxI

    if len(maxminI) == 1:
        stalls[maxminI[0]] = 1
    else:
        stalls[maxminI[maxmaxI[0]]] = 1
    return maxmax, maxmin

def doBF(n, k):
    stalls = [0 for x in xrange(n+2)]
    stalls[0] = 1
    stalls[n+1] = 1
    for kk in xrange(k):
        #print stalls,
        maxmax, maxmin = placeBF(stalls)
    #print stalls
    return str(maxmax)+" "+str(maxmin)
   
t = int(raw_input())
for i in xrange(1, t + 1):
    n, k = [int(x) for x in raw_input().split(" ")]
    #print n,k
    print "Case #%d: %s"%(i, doBF(n,k))

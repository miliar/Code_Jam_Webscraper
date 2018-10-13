"""B
   Google CodeJam 2010
"""

from datetime import datetime
from itertools import combinations

def routine(N, K, B, T, X, V):
    #work out how which chicks are between each chick and the end
    
    #work out finishing positions at T
    finish = [x + (V[i]*T)  for i, x in enumerate(X)]
    #print "finish", finish
    
    #adjust finishes for slow chicks
    blocked = [False] * N
    blockers = []
    for i, f in enumerate(finish):
        if f >= B: #possible to finish
            blockedby = 0
            for infront in finish[i+1:]:
                if infront < B:
                    blockedby += 1
            if blockedby:
                blockers.append(blockedby)
                blocked[i] = True
    blockers.sort()
    #print "blocked", blocked
    #print "blockers", blockers

    passed = len([f for i, f in enumerate(finish) if f >= B and not blocked[i]])
    swaps = 0
    while passed < K and blockers:
        swaps += blockers[0]
        passed += 1
        blockers.pop(0)
    
    if passed < K:
        return "IMPOSSIBLE"
    
    return swaps

if __name__ == '__main__':
    filename = "B-large"  #small-attempt0 large
    f = open(filename + ".in")
    fo = open(filename + ".out", "w")

    print datetime.now()

    c = int(f.readline().strip())
    print c, "cases"
    for case in xrange(c):
        N, K, B, T = [int(x) for x in f.readline().split()]
        print N, K, B, T
        
        X = [int(x) for x in f.readline().split()]
        print X

        V = [int(x) for x in f.readline().split()]
        print V

        print >>fo, "Case #%d: %s" % (case+1, routine(N, K, B, T, X, V))

    fo.close()
    f.close()
    print datetime.now()

import fileinput

import psyco
psyco.full()

class chicken(object):
    def __init__(self,x,v):
        self.x = x
        self.v = v
    def __repr__(self):
        return "chicken("+str(self.x)+","+str(self.v)+")"

def getColideTime(c0,c1,inf):
    if c0.x > c1.x:
        return inf
    colideTime = (c1.x-c0.x)/float(c0.v-c1.v)
    assert(colideTime > 0)
    return colideTime

def getCandidates(chickens,b,t):
    return [c for c in chickens if (b-c.x)/float(c.v) <= t]

def getClosestCandidates(chickens,b,t,k):
    candidates = getCandidates(chickens,b,t)
    #print candidates, k
    if len(candidates) < k:
        #print "Blat!"
        return -1
    return sorted(candidates,key=lambda c:c.x,reverse=True)[:k]

def getNumBlockingChickens(chickens,candidates,ourC,t):
    return len([c for c in chickens if c not in candidates and getColideTime(ourC,c,t+1) <= t])
    
def calcNumSwaps(chickens,b,t,k):
    swaps = 0
    candidates = getClosestCandidates(chickens,b,t,k)
    if candidates == -1:
        return -1
    candidates = set(candidates)
    for c in candidates:
        swaps += getNumBlockingChickens(chickens,candidates,c,t)
    return swaps

def initChickens(xs,vs):
    return [chicken(x,v) for x,v in zip(xs,vs)]

def main():
    it = fileinput.input()
    it.next()
    for (cn,l) in enumerate(it):
        (n,k,b,t) = [int(x) for x in l.split()]
        xs = [int(x) for x in it.next().split()]
        vs = [float(x) for x in it.next().split()]
        chickens = initChickens(xs,vs)
        swaps = calcNumSwaps(chickens,b,t,k)
        if swaps == -1:
            print "Case #%d: IMPOSSIBLE" % (cn+1)
        else:
            print "Case #%d: %d" % (cn+1,swaps)

if __name__ == "__main__":
    main()

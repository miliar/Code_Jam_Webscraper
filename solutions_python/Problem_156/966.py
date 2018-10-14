from sys import stdin

T = int(stdin.readline())

def standardize(P):
    P = sorted(P,reverse=True)
    while len(P)>1 and P[-1]==0:
        P.pop(-1)
    return P

class memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}
    def __call__(self, *args, **kwds):
        import cPickle
        str = cPickle.dumps(args, 1)+cPickle.dumps(kwds, 1)
        if not self.memo.has_key(str):
            self.memo[str] = self.fn(*args, **kwds)
        return self.memo[str]

@memoize
def F(P):
    if max(P) <= 1: return 1
    testP = P[:]
    for i in xrange(len(testP)):
        testP[i] = max(0,testP[i]-1)
    side1 = F(standardize(testP))
    
    side2 = 10000000000
    for numToMove in xrange(1,P[0]):
        testP = P[:]
        testP[0]-=numToMove
        testP.append(numToMove)
        side2 = min(side2,F(standardize(testP)))
    return 1 + min(side1,side2)
    
for trial in xrange(1,T+1):
    #sMax, digits = map(str, stdin.readline().split())
    D = int(stdin.readline())
    P = standardize(map(int, stdin.readline().split()))
    minutes=F(P)
    print "Case #%s: %s" % (trial,minutes)
    #print
        
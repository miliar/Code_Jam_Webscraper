def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

def testcase(cas=-1):
    D, N = readvals() 
    KSs = sorted( [readvals(float) for _ in xrange(N)], reverse = 1 )
    K, S = zip(*KSs)
    t = 0
    for i in xrange(N):
        t = max(t, (D-K[i])/S[i])
    res = D * 1. / t 
    print 'Case #%d: %.7f' % ( cas, res )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)

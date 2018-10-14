def readval(typ=int):
    return typ( raw_input() )

def readvals(typ=int):
    return map( typ, raw_input().split() )

def testcase(cas=-1):
    N, K = readvals()
    U = readval(float)
    P = readvals(float)
    P = sorted(P) 
    resP = []
    while P: 
        avg = ( sum(P)+U ) / len(P) 
        if avg >= P[-1]: # avg >= max proba: finish ! 
            resP.extend([avg]*len(P))
            P = [] 
        else: 
            resP.append( P.pop() )
    res = reduce(lambda a,b: a*b, resP)
    print 'Case #%d: %.9f' % ( cas, res )

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)

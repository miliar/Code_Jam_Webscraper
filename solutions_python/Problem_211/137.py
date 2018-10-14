def readvals(typ=int):
    return map(typ, raw_input().split())

def readval(typ=int):
    return typ(raw_input())

def testcase(case=-1):
    N, K = readvals()
    U = readval(float)
    P = sorted(readvals(float))
    results = []
    while P: 
        avg = (sum(P) + U) / len(P) 
        if avg >= P[-1]:
            results.extend([avg]*len(P))
            P = [] 
        else: 
            results.append( P.pop() )
    result = reduce(lambda a,b: a*b, results)
    print 'Case #%d: %.9f' % (case, result)

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)

def readvals(typ=int):
    return map( typ, raw_input().split() )

def readval(typ=int):
    return typ( raw_input() )

Len = 1440
def testcase(case=-1):
    Ac, Aj = readvals() 
    CD = [readvals() for _ in xrange(Ac)]
    JK = [readvals() for _ in xrange(Aj)]
    result = 0
    if Ac+Aj==1: 
        result = 2
    elif Ac==1 and Aj==1: 
        result = 2
    elif Ac==2:
        C, D = zip(*CD)
        l1 = (D[1] + Len - C[0]) % Len
        l2 = (D[0] + Len - C[1]) % Len 
        if l1 <= Len/2 or l2 <= Len/2: 
            result = 2
        else: 
            result = 4
    elif Aj==2:
        J, K = zip(*JK)
        l1 = (K[1] + Len - J[0]) % Len
        l2 = (K[0] + Len - J[1]) % Len 
        if l1 <= Len/2 or l2 <= Len/2: 
            result = 2
        else: 
            result = 4
    print 'Case #%d: %d' % (case, result)

if __name__=='__main__':
    T = readval()
    for i in xrange(T):
        testcase(i+1)

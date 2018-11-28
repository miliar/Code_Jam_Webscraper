def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())

import time
def main(fn1, fn2):
    startTime = time.time()
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                N,K = parseTuple(f)
                print N,K
                U = parseScalar(f,float)
                Pi = list(parseTuple(f,float))
                # if K<N:
                #     continue
                x = solveSmall(N,K,U,Pi)
                print>>g, 'Case #%d: %f'  % (n+1, x)
                print 'Case #%d: %f'  % (n+1, x)
                print 'Computed in %d seconds'%(time.time()-startTime)


import sys, random, math, numpy

def solveSmall(N,K,U,Pi):
    assert K==N
    Pi.sort()
    cs = numpy.cumsum(Pi)
    print Pi
    print U
    print cs
    shift = numpy.zeros(cs.shape)
    s = len(Pi)-1
    for i in range(1,len(Pi)):
        shift[i] =  (i)*Pi[i] - cs[i-1]
        if shift[i] > U:
            s = i-1
            break
    print shift
    #s is the index to which we bring all the previous ones
    slack = U-shift[s]
    print s, U, slack
    level = min(1.0, Pi[s] + slack / (s+1))
    print level
    for i in range(s+1):
        Pi[i] = level
    sc = 1.0
    for p in Pi:
        sc *= p
    return sc








if __name__ == '__main__':
    #solveRand(16,50)
    #main('C-test.in', 'C-test.out')
    #main('C-test-large.in', 'C-test-large.out')
    main('C-small-1-attempt1.in', 'C-small-1-attempt1.out')
    #main('C-large.in', 'C-large.out')
    sys.exit(0)



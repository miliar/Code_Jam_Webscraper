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
                ma,mi = solve(N,K)
                print>>g, 'Case #%d: %d %d'  % (n+1, ma, mi)
                print 'Case #%d: %d %d'  % (n+1, ma, mi)

    print 'Computed in %d seconds'%(time.time()-startTime)


import sys, random, math

def solve(N,K):
    level = int(math.ceil(math.log(K+1,2)))
    assert 2**level > K and 2**(level-1) <= K
    divisor = 2**(level-1)
    taken = divisor-1
    small,rest = divmod(N-taken,divisor)
    if K-taken <= rest:
        cellSize = small+1
    else:
        cellSize = small
    print N,K,level,divisor,taken,small,rest, K-taken, cellSize
    halfCell = float(cellSize-1)/2.0
    return int(math.ceil(halfCell)),int(math.floor(halfCell))


if __name__ == '__main__':

    #main('C-test.in', 'C-test.out')
    #main('C-test-large.in', 'C-test-large.out')
    main('C-small-2-attempt0.in', 'C-small-2-attempt0.out')
    #main('C-large.in', 'C-large.out')
    sys.exit(0)



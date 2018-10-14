def parseScalar(f,c=int):
    return c(f.next().strip('\r\n'))
def parseTuple(f,c=int):
    return tuple(c(s) for s in  f.next().strip('\r\n').split())


def main(fn1, fn2):
    with open(fn1) as f:
        with open(fn2, 'w') as g:
            ncases = parseScalar(f)
            for n in range(ncases):
                i = parseScalar(f)
                x = solve(i)
                x = ''.join(str(d) for d in x)
                print>>g, 'Case #%d: %s'  % (n+1,str(x))
                print 'Case #%d: %s'  % (n+1,str(x)  )

def test_nice(digits):
    if len(digits)==0:
        return True
    for i in range(1,len(digits)):
        if digits[i] < digits[i-1]:
            return False
    return True

import sys, itertools
def solve(i):
    s = str(i)
    N = len(s)
    digits = [int(c) for c in str(i)]
    if test_nice(digits):
        return digits
    # finds largest nice prefix
    for prefLen in range(len(digits),0,-1):
        d2 = digits[:prefLen]
        if test_nice(d2):
     #       print prefLen,d2
            if prefLen > 1 and d2[-1] > d2[-2]  or prefLen == 1 and d2[0] > 1:
                d3 = d2[:-1] + [d2[-1]-1] + [9]*(N-prefLen)
    #            print 'Found', d3
                assert len(d3) == N
                return d3
    # test whether d2's last digit can be decremented by one
   # print 'reduce'
    d3 = [9]*(N-1)
    return d3





if __name__ == '__main__':
    #main('B-test.in', 'B-test.out')
    #main('B-small-attempt0.in', 'B-small-attempt0.out')
    main('B-large.in', 'B-large.out')
    sys.exit(0)



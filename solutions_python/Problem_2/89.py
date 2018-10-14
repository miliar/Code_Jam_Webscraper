import sys
from array import array

class MyException(Exception):
    pass

def parseTime(s):
    [h1, m1, h2, m2] = map(lambda x: int(x), (s[0] + ':' + s[1]).split(':'))
    return (h1*60 + m1, h2*60 + m2)

def main():
    N = int(sys.stdin.readline())
    for case in xrange(N):
        T  = int(sys.stdin.readline())
        [NA, NB] = [int(x) for x in sys.stdin.readline().split()]
        a2b = [parseTime(sys.stdin.readline().split()) for i in xrange(NA)]
        b2a = [parseTime(sys.stdin.readline().split()) for i in xrange(NB)]
        a2b.sort()
        b2a.sort()
        for x in xrange(NA): 
            if x + 1 < NA: assert(a2b[x][0] <= a2b[x + 1][0])
        for x in xrange(NB): 
            if x + 1 < NB: assert(b2a[x][0] <= b2a[x+1][0])
        res = (NA, NB)
        for na in xrange(NA + NB + 2):
            for nb in xrange(NA + NB + 2):
                if na + nb > res[0] + res[1]: continue
                try:
                     a = array('i', [0 for j in xrange(24*60 + 60)])
                     b = array('i', [0 for j in xrange(24*60 + 60)])
                     a[0], b[0] = na, nb
                     ia, ib = 0, 0
                     for t in xrange(24*60):
                         xa, xb = a[t], b[t]
                         while ia < NA and a2b[ia][0] == t: 
                             if xa == 0: raise MyException
                             xa -= 1
                             b[a2b[ia][1] + T] += 1
                             ia += 1
                         while ib < NB and b2a[ib][0] == t: 
                             if xb == 0: raise MyException
                             xb -= 1
                             a[b2a[ib][1] + T] += 1
                             ib += 1
                         a[t+1] += xa
                         b[t+1] += xb
                except MyException:
                    pass
                else:
                    if res[0] + res[1] > na + nb:
                        res = (na, nb)
                

        print 'Case #%d: %d %d' % (case + 1, res[0], res[1])
main()
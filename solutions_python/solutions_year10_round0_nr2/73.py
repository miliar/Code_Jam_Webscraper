import sys

def gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

fin = open(sys.argv[1], 'r')
C = int(fin.readline())
for i in xrange(C):
    testcase = fin.readline().split()
    N = int(testcase[0])
    t = [long(x) for x in testcase[1:]]
    
    t.sort()
    base = t[0]
    t = [t[j] - t[j-1] for j in xrange(1, len(t))]
    #print t

    g = reduce(gcd, t[1:], t[0])
    #print g
    
    res = (base // g) * g
    if res < base:
        res += g
    assert res >= base
    res -= base
    print 'Case #%d: %d' % (i+1, res)

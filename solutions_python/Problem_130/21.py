from sys import stdin
from itertools import permutations
def solve():
    read_ints = lambda: map(int, stdin.readline().split())
    n, p = read_ints()
    if p == 1 << n:
        print 2 ** n - 1, 2 ** n - 1
        return
    t = k = 0
    p -= 1
    for i in reversed(xrange(n)):
        if p < t: break
        t += 1 << i
        k += 1 << (n - i - 1)
    print k - 1,
    t = k = 2 ** n - 1
    for i in xrange(n):
        if p >= t: break
        k -= 1 << i
        t -= 1 << (n - i - 1)
    print k
    """
    a1 = [0] * (2**n)
    a2 = [2**n-1] * (2**n)
    for x in permutations(xrange(2**n)):
        y = x[:]
        for t in xrange(n):
            w = []
            l = []
            for i in xrange((2**n)/2):
                w.append(min(y[i*2], y[i*2+1]))
                l.append(max(y[i*2], y[i*2+1]))
            y = w + l
        for i in xrange(2**n):
            a1[y[i]] = max(i, a1[y[i]])
            a2[y[i]] = min(i, a2[y[i]])
        #print x, y
    print a1, a2
    """
T = int(stdin.readline())
for i in xrange(0, T):
    print "Case #%d:" % (i+1), 
    solve()

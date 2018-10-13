S = [0,1,2,3]
T = [(1,1,10,2),(2,2,10,8)]

for i in xrange(50):
    S += [a[0] * a[2] + a[1] for a in T]
    S += [a[0] * 10 * a[2] + v * a[2] + a[1] for a in T for v in xrange(3) if a[3] + v * v < 10]
    T = [(a[0] * 10 + j, j * a[2] + a[1], 10 * a[2], a[3] + 2 * j * j) for a in T for j in xrange(3) if a[3] + 2 * j * j < 10]

S = [z * z for z in S]

def f(n):
    isLessThan = 0
    isntLessThan = len(S) - 1
    while isLessThan + 1 < isntLessThan:
        test = (isLessThan + isntLessThan) / 2
        if (S[test] < n):
            isLessThan = test
        else:
            isntLessThan = test
    return isLessThan

def g(n,k):
    return f(k+1)-f(n)

from sys import stdin

for i in xrange(1,1+int(stdin.readline())):
    [a, b] = [int(z) for z in stdin.readline().split()]
    print "Case #%d: %d" % (i, g(a, b))

from sys import stdin

def gcd(A, B):
    a = A
    b = B
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

if __name__ == '__main__':
    C = int(stdin.readline())
    for c in xrange(1, C + 1):
        a = stdin.readline().split()
        N = int(a[0])
        t = map(long, a[1:])
        first = t[0]
        for i in xrange(N - 1):
            t[i] = abs(t[i] - t[i + 1])
        t[-1] = abs(t[-1] - first)
        T = t[-1]
        for i in xrange(N - 1):
            T = gcd(T, t[i])
        if first % T == 0:
            y = 0
        else:
            y = T - first % T
        print "Case #%d: %d" % (c, y) 

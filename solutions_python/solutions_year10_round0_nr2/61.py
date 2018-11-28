import sys

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

f = open(sys.argv[1])
tst = int(f.readline())
for t in xrange(0, tst):
    ar = f.readline().split();
    k = int(ar[0])
    a = [];
    for i in xrange(0, k):
        a.append(long(ar[i + 1]))

    res = abs(a[1] - a[0])
    for i in xrange(1, k - 1):
        res = gcd(res, abs(a[i + 1] - a[i]))

    resy = (res - a[0] % res) % res

    print "Case #" + str(t + 1) + ":", resy
    
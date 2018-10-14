import sys

def ints(): return [int(x) for x in sys.stdin.readline().split()]

[T] = ints()

for i in xrange(T):
    inp = ints()
    n = inp[0]
    t = inp[1:]
    t.sort()
    base = t[0]
    k = 0
    for x in t:
        def gcd(a, b): return a if b == 0 else gcd(b, a % b)
        k = gcd(k, x - base)
    y = (k - base % k) % k
    print ("Case #%d: %s" % (i+1, y))

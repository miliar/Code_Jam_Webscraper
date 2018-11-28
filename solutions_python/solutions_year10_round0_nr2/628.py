import sys

def gcd(a,b):
    if a < b:
        a, b = b, a
    while a % b > 0:
        a, b = b, a % b
    return b

def compute(n, t):
    d = abs(t[0] - t[1])
    k = d
    for i in xrange(2, n):
        m = abs(t[i] - t[i-1])
        if m == 0:
            continue
        if d == 0:
            k = m
            d = m
            continue
        k = gcd(d, m)
        d = m        
    return (k - (t[0] % k)) % k

if __name__ == '__main__':
    f = open(sys.argv[1])
    c = int(f.readline())
    for i in xrange(c):
        arr = map(int, f.readline().split())
        n = arr[0]
        t = arr[1:]
        print "Case #%d: %d" % (i+1, compute(n, t))
    f.close()
    


def cGCD(a, b):
    while b:
        a, b = b, a % b
    return a

T = int(raw_input())

for tn in xrange(T):
    l = raw_input().split()
    n = int(l[0])
    t = []
    for i in xrange(1, n+1):
        t.append(long(l[i]))
    t.sort(reverse=True)

    GCD = 0
    for i in xrange(n-1):
        if not GCD:
            GCD = t[i] - t[i+1]
        else:
            GCD = cGCD(GCD, t[i] - t[i+1])

    print 'Case #%d: %d' % (tn+1, (-t[n-1]) % GCD)

from fractions import gcd

C = int(raw_input())

for c in xrange(C):
    Ts = map(int, raw_input().split(' '))
    N = Ts.pop(0)

    Ts.sort()
    
    deltas = set()
    for i in xrange(N-1):
        deltas.add(Ts[i+1] - Ts[i])

    T = reduce(gcd, deltas)

    y = ((T - Ts[0]) % T)
        
    print "Case #%d: %d" % (c+1, y)


def gcd(a,b):
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)

c = int(raw_input())
for i in range(c):
    items = raw_input().strip().split()
    n = int(items[0])
    ts = [int(x) for x in items[1:]]
    m = min(ts)
    xs = sorted([t-m for t in ts])
    g = gcd(xs[1],xs[0])
    for j in range(n-2):
        g = gcd(g,xs[j+2])

    #print g, m

    if g < m:
        out = g * ((m+g-1) / g)
    else:
        out = g

    print "Case #%d: %d" % (i+1, out - m)

    

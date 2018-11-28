def gcd(a, b):
    if b==0:
        return a
    if a%b==0:
        return b
    return gcd(b, a%b)

n=int(raw_input())
for kk in range(n):
    w=[int(i) for i in raw_input().split()]
    w = w[1:]
    w.sort()
#    print w[0], w[1]
    t = 0
    for i in range(len(w)-1):
        t = gcd(w[i+1]-w[i], t)
    e = t-(w[0]%t)
    if e==t:
        e=0
    print "Case #%d: %d" % (kk+1, e)

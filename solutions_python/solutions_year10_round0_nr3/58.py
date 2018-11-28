import sys

def ints(): return [int(x) for x in sys.stdin.readline().split()]

[T] = ints()

for cs in xrange(T):
    (R, k, N) = ints()
    g = ints()
    def fill(p, a):
        total = 0
        for (i, x) in enumerate(a):
            if total + x > k: return ((p + i) % N, total)
            total += x
        return (p, total)
    
    next = [fill(i, g[i:]+g[:i]) for i in range(N)]
    crumb = [None]*N
    i, euro = 0, 0
    r = 0
    while r < R and not crumb[i]:
        crumb[i] = r, euro
        i, deuro = next[i]
        euro += deuro
        r += 1
    if r < R:
        dr, deuro = r - crumb[i][0], euro - crumb[i][1]
        jump = (R - r) / dr
        r += jump * dr
        euro += jump * deuro
    while r < R:
        crumb[i] = r, euro
        i, deuro = next[i]
        euro += deuro
        r += 1
    print ("Case #%d: %s" % (cs+1, euro))

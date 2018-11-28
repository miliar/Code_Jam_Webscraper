def draw(r, t):
    ink = 2 * r + 1
    if t >= ink:
        return t - ink
    return None

def calc(r, t):
    n = 0
    while t:
        t = draw(r, t)
        if t is None:
            return n
        n += 1
        r += 2
    return n

T = int(raw_input())
for i in xrange(T):
    r, t = map(int, raw_input().strip().split())
    print "Case #{0}: {1}".format(i + 1, calc(r, t))

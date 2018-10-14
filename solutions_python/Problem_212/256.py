t = int(raw_input())

def cache(f):
    c = dict()
    def g(*args):
        targs = tuple(args)
        if targs not in c:
            c[targs] = f(*args)
        return c[targs]
    return g

@cache
def dp3(r1, r2, rem):
    if r1 == r2 and r2 == 0:
        return 0
    m = -1
    if r1 > 0:
        m = max(m, dp3(r1-1, r2, (rem + 1) % 3) + (1 if rem % 3 == 0 else 0))
    if r2 > 0:
        m = max(m, dp3(r1, r2-1, (rem + 2) % 3) + (1 if rem % 3 == 0 else 0))
    return m

for kei in xrange(1, t+1):
    g, p = [int(x) for x in raw_input().split(' ')]
    arr = [int(x) for x in raw_input().split(' ')]
    if p == 2:
        tot = sum(1 for x in arr if x % 2 == 0)
        ext = len(arr) - tot
        tot += ext / 2
        tot += 1 if ext % 2 == 1 else 0
    elif p == 3:
        rem = [0]*3
        for i in arr:
            rem[i%3] += 1
        tot = rem[0] + dp3(rem[1], rem[2], 0)
    print "Case #%d: %d" % (kei, tot)

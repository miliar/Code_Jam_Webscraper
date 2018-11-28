n = int(raw_input())

def solve(l):
    s = 0
    k = 0
    for i, a in enumerate(l):
        if i > s:
            k += i - s
            s += i - s
        s += a
    return k

for c in xrange(1, n+1):
    m, s = raw_input().split()
    a = [int(x) for x in s]
    print "Case #{0}: {1}".format(c, solve(a))



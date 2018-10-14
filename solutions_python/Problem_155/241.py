rl = lambda: map(int, raw_input().split())


def solve(s):
    n = 0
    m = 0
    for i, c in enumerate(s):
        m = max(m, (i - n))
        n += int(c)
    return m

t = input()
for nt in xrange(t):
    s = raw_input().split()[-1]
    res = solve(s)
    print "Case #%d:" % (nt + 1), res

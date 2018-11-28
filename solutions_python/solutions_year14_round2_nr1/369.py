rl = lambda: map(int, raw_input().split())


def ssplit(s):
    res = []
    prev = None
    n = 0
    for c in s:
        if c == prev:
            n += 1
        else:
            if prev:
                res.append((prev, n))
            prev = c
            n = 1
    if prev:
        res.append((prev, n))
    return zip(*res)


def solve(sl):
    a = None
    l = []
    for s in sl:
        r, c = ssplit(s)
        if a is not None and a != r:
            return None
        l.append(c)
        a = r

    res = 0
    for m in zip(*l):
        mz = 1000000000
        for k in xrange(1, 101):
            mt = sum(abs(x - k) for x in m)
            mz = min(mz, mt)
        res += mz
    return res


t = input()
for nt in xrange(t):
    n = input()
    ss = [raw_input() for _ in xrange(n)]
    res = solve(ss)
    print "Case #%d:" % (nt + 1),
    if res is None:
        print "Fegla Won"
    else:
        print res

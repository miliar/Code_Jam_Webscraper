t = int(raw_input())

ctnum = lambda x: len(str(x))

for j in xrange(t):
    a, b = (int(x) for x in raw_input().split(' '))
    num = ctnum(a)
    shift = lambda x: (x / 10) + (x % 10) * (10 ** (num - 1))
    pairs = set()
    for i in xrange(a, b + 1):
        w = i
        for k in xrange(num):
            if (w < i) and (w in xrange(a, b + 1)) and ctnum(w) == ctnum(i):
                pairs.add((i, w))
            w = shift(w)
    print 'Case #%s: %s' % (j + 1, len(pairs))


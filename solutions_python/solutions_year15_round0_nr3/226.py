rl = lambda: map(int, raw_input().split())

o, i, j, k = range(1, 5)

t_mul = [
    [],
    [0, 1, i, j, k],
    [0, i, -1, k, -j],
    [0, j, -k, -1, i],
    [0, k, j, -i, -1]
]

sign = lambda x: -1 if x < 0 else 1
mul = lambda a, b: t_mul[abs(a)][abs(b)] * sign(a) * sign(b)
lmul = lambda l: reduce(mul, l, 1)


def check(l):
    s = 1
    ifound = False
    v = lmul(l)
    if v != -1:
        return False
    # print 'check', l, v
    for x in l:
        s = mul(s, x)
        # print s,
        if ifound:
            if mul(s, k) == v:
                return True
        else:
            ifound = (s == i)
    return False


def solve(s, x):
    s = map('  ijk'.index, s)
    v = lmul(s)

    ok = lambda x, s: x >= s and (x - s) % 4 == 0

    for a in xrange(0, 4):
        for b in xrange(0, 4):
            for c in xrange(0, 4):
                if ok(x, a + b + c + 2) and \
                        check([v] * a + s + [v] * b + s + [v] * c):
                    return 1

            if ok(x, a + b + 1) and check([v] * a + s + [v] * b):
                return 1
    return 0

t = input()
for nt in xrange(t):
    l, x = rl()
    s = raw_input().strip()
    res = solve(s, x)
    print "Case #%d:" % (nt + 1), ['NO', 'YES'][res]

import sys

f = open('A-small-attempt0.in')
o = open('A-small-attempt0.out', 'w')
T = int(f.readline().strip())

CONSO = 'bcdfghjklmnpqrstvwxyz'


def all_con(s):
    for c in s:
        if c not in CONSO:
            return False
    return True


def subs(s, n):
    lcon = [s[i:i+n] for i in range(len(s) - n + 1) if all_con(s[i:i+n])]
    for l in range(n, len(s) + 1):
        for i in range(len(s) + 1 - l):
            ss = s[i:i + l]
            for con in lcon:
                if con in ss:
                    yield (i, i + l)


def write(s):
    o.write(s)
    sys.stdout.write(s)


def solve():
    for t in xrange(T):
        m = f.readline().strip().split(' ')

        p = c(m)

        res = p
        s = "Case #%d: %s\n" % (t + 1, res)
        write(s)


def c(m):
    ss, n = m[0], int(m[1])
    return len(set(subs(ss, n)))

solve()

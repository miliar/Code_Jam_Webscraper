import sys
import psyco
psyco.full()

def subsets_i(s, n):
    n_elems = len(s)
    n_subsets = 2 ** len(s)
    for i in range(0, n_subsets):
        sub = []
        for j in range(0, n_elems):
            if (i >> j & 1):
                sub.append(s[j])
        if sub != [] and n in sub:
            yield sub

def process(ss, n):
    n = ss.index(n) + 1
    if n == 1:
        return True
    while n in ss:
        n = ss.index(n) + 1
    if n == 1:
        return True
    return False

p = {
    2: 1,
    3: 2,
    4: 3,
    5: 5,
    6: 8,
    7: 14,
    8: 24,
    9: 43,
    10: 77,
    11: 140,
    12: 256,
    13: 472,
    14: 874,
    15: 1628,
    16: 3045,
    17: 5719,
    18: 10780,
    19: 20388,
    20: 38674,
    21: 73562,
    22: 40265,
    23: 68060,
    24: 13335,
    25: 84884
}

cases = int(sys.stdin.readline().strip())
for case in xrange(1, cases + 1):
    n = int(sys.stdin.readline().strip())
    if n in p.keys():
        print 'Case #%d: %d' % (case, p[n])
        continue
    t = 0
    for ss in subsets_i(range(2, n + 1), n):
        if process(ss, n):
            t += 1
            t %= 100003
    p[n] = t
    print 'Case #%d: %d' % (case, t)
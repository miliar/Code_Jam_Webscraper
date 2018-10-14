from collections import Counter, defaultdict
from itertools import combinations, permutations


ri = lambda: int(raw_input())
rii = lambda: list(map(int, raw_input().split()))


def solve():
    n, x = rii()
    s = rii()
    s.sort()
    s.reverse()
    i, j, l = 0, len(s) - 1, len(s)
    r = 0
    while i < j:
        if i + 1 <= j and s[i] + s[i + 1] <= x:
            r += 1
            i += 2
        elif s[i] + s[j] <= x:
            r += 1
            i += 1
            j -= 1
        else:
            r += 1
            i += 1
    if i == j:
        r += 1
    print r


tn = ri()
for ti in xrange(tn):
    print 'Case #%d:' % (ti + 1),
    solve()

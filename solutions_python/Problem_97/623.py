import sys
from collections import defaultdict


memoize = defaultdict(list)

def count(n, b, gs):
    nn = n
    if nn in memoize:
        cc = 0
        for m in memoize[nn]:
            pair = (n, m)
            if pair not in gs and int(m) <= b:
                gs.add(pair)
                cc += 1
        return cc

    n = str(n)
    s = n + n
    cc = 0
    for i in range(1, len(n)):
        if n[i] >= n[0]:
            m = s[i:i+len(n)]
            pair = (n, m)
            if m > n:
                memoize[nn].append(m)
                if pair not in gs and int(m) <= b:
                    gs.add(pair)
                    cc += 1
    return cc

def recycle(a, b):
    gs = set()
    return sum(count(n, b, gs) for n in range(a, b))


s = sys.stdin.readlines()[1:]

for i in range(len(s)):
    a, b = map(int, s[i].strip().split())
    print 'Case #' + str(i+1) + ':', recycle(a, b)

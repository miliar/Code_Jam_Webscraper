#!/usr/bin/env python2

def solve():
    ns = raw_input()
    outcomes = [str(int(ns[:i]) - 1).lstrip('0') + '9' * (len(ns) - i) for i in range(1, len(ns))]
    outcomes.append(ns)
    ok = [o for o in outcomes if sorted(o) == list(o)]
    return max(ok, key=int)

t = int(raw_input())
for i in range(1, t + 1):
    print 'Case #{}: {}'.format(i, solve())

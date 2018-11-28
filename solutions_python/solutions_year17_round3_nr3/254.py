#!/usr/bin/env python

def solve(U, ps, pap=1.0):
    if len(ps) == 0:
        return pap
    avg = min(1, (sum(ps) + U) / len(ps))
    pabove = []
    pbelow = []
    for p in ps:
        if p > avg:
            pabove.append(p)
            pap *= p
        else:
            pbelow.append(p)
    if pabove:
        return solve(U, pbelow, pap)
    else:
        return pap * avg**len(ps)


T = int(raw_input().strip())
for t in range(T):
    N, K = [int(x) for x in raw_input().strip().split()]
    U = float(raw_input().strip())
    p = [float(x) for x in raw_input().strip().split()]
    print 'Case #%d: %f' % (t+1, solve(U, p))

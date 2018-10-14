def streamify(lst):
    while True:
        for e in lst: yield e

def find_period(k, gs):
    period_list = []
    seen = {}
    start = 0
    ct = 0
    idx = 0
    size = len(gs)
    gs_stream = streamify(gs)
    acc = gs_stream.next()
    for g in gs_stream:
        if start in seen:
            return seen[start], period_list
        else:
            if acc + g > k: 
                period_list.append(acc)
                seen[start] = idx
                acc = 0
                start = (ct + 1) % size
                idx += 1
            ct += 1
            acc += g

def run(R, k, gs):
    if sum(gs) <= k:
        start = 0
        period_list = [sum(gs)]
    else:
        start, period_list = find_period(k, gs)
    period_length = len(period_list) - start
    period_sum = sum(period_list[start:])
    if R <= start: return sum(period_list[:R])
    num_period, period_rem  = (R - start) / period_length, (R - start) % period_length
    return num_period * period_sum + sum(period_list[start:(start + period_rem)])\
            + sum(period_list[:start])

import sys
f = open(sys.argv[1])
num_cases = int(f.next())
for i in xrange(1, num_cases + 1):
    R, k, N = f.next().split(' ', 3)
    R = int(R)
    k = int(k)
    N = int(N)
    gs = [int(x) for x in f.next().split(' ')]
    print 'Case #%i: %i'%(i, run(R, k, gs))

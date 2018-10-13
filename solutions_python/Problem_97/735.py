__author__ = 'Sebastian Poreba'

from collections import deque

N = int(raw_input())

for test in xrange(0, N):
    input = [int(x) for x in (raw_input().split())]
    A = input[0]
    B = input[1]
    results = [0] * (B+2)
    for i in xrange(A,B):
        q = [c for c in str(i)]
        mid_results = {}
        for j in xrange(0, len(str(i))):
            q = q[1:] + [q[0]]
            if q[0] == 0: continue
            numeric = int(''.join(q))
            if B >= numeric > i:
                mid_results[numeric] = numeric
        for res in mid_results:
            results[res] += 1
    print 'Case #%d: %d' % (test+1, sum(results))


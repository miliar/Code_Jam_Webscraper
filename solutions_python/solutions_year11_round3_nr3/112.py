#!/usr/bin/env python

from multiprocessing import Pool, cpu_count

def solve(params):
    N, L, H = params[0]
    freq = params[1]

    for f in xrange(L, H+1):
        correct = True
        for p in freq:
            if f%p != 0 and p%f != 0:
                correct = False
                break
        if correct:
            return str(f)

    return 'NO'

if __name__ == '__main__':
    T = int(raw_input())

    testcases = []
    for t in range(T):
        N, L, H = [int(x) for x in raw_input().split()]
        freq = [int(x) for x in raw_input().split()]
        assert len(freq) == N
        testcases.append([(N,L,H), freq])

    pool = Pool(cpu_count())
    results = pool.map(solve, testcases)

    for t in range(T):
        print 'Case #{0}: {1}'.format(t+1, results[t])


from collections import defaultdict
import sys
inp = sys.stdin.readlines()

cases = int(inp.pop(0))
for case in range(1, cases + 1):
    N, K = inp.pop(0).strip().split()
    N = int(N)
    K = int(K)

    buckets = defaultdict(lambda: 0)
    buckets[N] = 1
    while K > 0:
        n = max(buckets.keys())
        c = buckets[n]
        del buckets[n]
        L = (n - 1) // 2
        R = n // 2
        buckets[L] += c
        buckets[R] += c
        K -= c
    result = '{} {}'.format(max(L, R), min(L, R))
    print 'Case #{}: {}'.format(case, result)

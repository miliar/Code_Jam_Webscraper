import sys
from collections import defaultdict

def solve(n, person_k):
    person = 0
    last = {n:1}
    while True:
        cur = defaultdict(int)
        for k in sorted(last.keys(), reverse=True):
            v = last[k]
            k -= 1
            person += v
            left = k / 2
            right = k - left
            if person >= person_k:
                return str(right), str(left)
            cur[left] += v
            cur[right] += v
        last = cur

t = int(next(sys.stdin))
for test in range(t):
    s = next(sys.stdin).strip()
    n, k = [int(_) for _ in s.split(' ')]
    print ('Case #{}: {}'.format(test+1, ' '.join(solve(n, k))))

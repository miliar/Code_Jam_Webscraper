import sys
from collections import defaultdict

def spaces(n):
    return n//2, n//2 - (1 if n%2 == 0 else 0)

_cache = {}
def solve(n,k,depth=0):
    if (n,k) in _cache:
        return _cache[(n,k)]

    gaps = [(n,1)]
    last = None
    while k > 0:
        ngaps = defaultdict(int)
        for g,c in gaps:
            g1,g2 = spaces(g)
            last = (g1,g2)
            k -= c
            if k <= 0:
                break
            ngaps[g1] += c
            ngaps[g2] += c
        gaps = sorted(((g,c) for g,c in ngaps.items()), reverse=True)

    ans = max(last), min(last)
    _cache[(n,k)] = ans
    return ans

if __name__ == '__main__':
    lines = sys.stdin.readlines()[1:]
    for t,l in enumerate(lines):
        print('Case #{}: {}'.format(t+1,' '.join(str(x) for x in solve(*(int(n) for n in l.split())))))

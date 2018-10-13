from functools import lru_cache, partial

flip_trans = str.maketrans('+-', '-+')

def flip(s, n, k=None):
    return s[:n] + s[n:n+k].translate(flip_trans) + s[n+k:]


# @lru_cache(maxsize=None)
def solve(s, k):

    fl = partial(flip, k=k)

    @lru_cache(maxsize=None)
    def _solve(s):
        s = s.strip('+')

        if not s:
            return 0

        if len(s) < k:
            return None

        subs = [_solve(fl(s, 0)), _solve(fl(s, len(s) - k))]
        subs = [s for s in subs if s is not None]

        if not subs:
            return None
        else:
            return 1 + min(subs)

    return _solve(s)


from pathlib import Path
import sys

from tqdm import trange

def main():
    sys.setrecursionlimit(15000)
    ip = sys.argv[1]
    lines = (l.strip() for l in open(ip))
    t = int(next(lines))
    
    lines = (l.split() for l in lines)
    cases = ((l[0], int(l[1])) for l in lines)

    results = ((i+1, solve(*next(cases))) for i in trange(t))

    with open(Path(ip).with_suffix('.out').name, mode='w') as op:
        for i, r in results:
            if r is None:
                r = 'IMPOSSIBLE'
            print(f'Case #{i}: {r}', file=op)

main()

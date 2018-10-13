import sys
assert sys.version_info >= (3, 5)
from collections import Counter


def solve(prefix):
    N, K = [int(_) for _ in input().split()]
    lv = ((N, 1),)
    k = 1
    while K > k:
        assert sum(t[1] for t in lv) == k
        assert 1 <= len(lv) <= 2
        assert len(lv) == 1 or lv[0][0] == lv[1][0]+1
        K -= k
        k <<= 1
        nlv = Counter()
        for nn, kk in lv:
            nlv[nn>>1] += kk
            nlv[((nn+1)>>1)-1] += kk
        lv = tuple(sorted(nlv.items(), key=lambda t: t[0], reverse=True))
    n = lv[0][0] if K <= lv[0][1] else lv[1][0]
    print('{}{} {}'.format(prefix, n>>1, ((n+1)>>1)-1))


def main():
    T = int(input())
    for t in range(T):
        solve(prefix='Case #{}: '.format(t+1))


if __name__ == '__main__':
    main()

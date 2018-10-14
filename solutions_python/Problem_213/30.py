#!/usr/bin/env python3

from collections import Counter

TEST = 'large'
IN = 'B-{}.in'.format(TEST)
OUT = 'B-{}.out'.format(TEST)


def check(r, n, c, t):
    pp = [p for p, b in t]
    pp.sort()
    i = 0
    free = 0
    pro = 0
    for s in range(n):
        q = 0
        while i < len(pp) and pp[i] == s:
            q += 1
            i += 1
        if q > r + free:
            return None
        if q > r:
            free -= q - r
            pro += q - r
        else:
            free += r - q
    return pro


def run(n, c, t):
    ct = Counter(b for p, b in t)
    low = max(ct.values()) - 1
    high = len(t)
    while high - low > 1:
        mid = (low + high) // 2
        res = check(mid, n, c, t)
        if res is None:
            low = mid
        else:
            high = mid
    res = check(high, n, c, t)
    return '{} {}'.format(high, res)


def main():
    with open(IN) as fin, open(OUT, 'w') as fout:
        t = int(fin.readline().strip())
        for i in range(t):
            n, c, m = map(int, fin.readline().split())
            tick = [tuple(int(x) - 1 for x in fin.readline().split()) for j in range(m)]
            res = run(n, c, tick)
            print('Case #{}: {}'.format(i + 1, res), file=fout)


if __name__ == '__main__':
    main()

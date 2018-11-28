#!/usr/bin/env python3

TEST = 'large'
IN = 'C-{}.in'.format(TEST)
OUT = 'C-{}.out'.format(TEST)


def run(n, k):
    runs = {n: 1}
    while k > 0:
        mr = max(runs.keys())
        if runs[mr] < k:
            m = runs[mr]
            del runs[mr]
        else:
            m = k
            runs[mr] -= k
        y, z = mr // 2, (mr - 1) // 2
        runs.setdefault(y, 0)
        runs.setdefault(z, 0)
        runs[y] += m
        runs[z] += m
        k -= m
    return '{} {}'.format(y, z)


def main():
    with open(IN) as fin, open(OUT, 'w') as fout:
        t = int(fin.readline().strip())
        for i in range(t):
            n, k = map(int, fin.readline().split())
            res = run(n, k)
            print('Case #{}: {}'.format(i + 1, res), file=fout)


if __name__ == '__main__':
    main()

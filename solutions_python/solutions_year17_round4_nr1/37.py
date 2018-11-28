#!/usr/bin/env python3

TEST = 'large'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)


def run(p, g):
    rem = [0] * p
    for gi in g:
        rem[gi % p] += 1
    fresh = 0
    
    fresh += rem[0]
    rem[0] = 0

    if p % 2 == 0:
        q = rem[p // 2] // 2
        fresh += q
        rem[p // 2] -= 2 * q

    if p > 2:
        q = min(rem[1], rem[p - 1])
        fresh += q
        rem[1] -= q
        rem[p - 1] -= q

        if p % 2 == 0 and rem[p // 2] > 0 and max(rem[1], rem[p - 1]) >= p // 2:
            fresh += 1
            rem[p // 2] -= 1
            if rem[1] >= p // 2:
                rem[1] -= p // 2
            else:
                rem[p - 1] -= p // 2

        q = rem[1] // p
        fresh += q
        rem[1] -= p * q

        q = rem[p - 1] // p
        fresh += q
        rem[p - 1] -= p * q

    if any(rem):
        fresh += 1

    return fresh


def main():
    with open(IN) as fin, open(OUT, 'w') as fout:
        t = int(fin.readline().strip())
        for i in range(t):
            n, p = map(int, fin.readline().split())
            g = list(map(int, fin.readline().split()))
            res = run(p, g)
            print('Case #{}: {}'.format(i + 1, res), file=fout)


if __name__ == '__main__':
    main()

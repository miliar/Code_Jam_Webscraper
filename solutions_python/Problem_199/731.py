#!/usr/bin/env python3

TEST = 'large'
IN = 'A-{}.in'.format(TEST)
OUT = 'A-{}.out'.format(TEST)


def run(s, k):
    s = [c == '+' for c in s]
    flips = 0
    for i, c in enumerate(s):
        if not c:
            if i + k > len(s):
                return 'IMPOSSIBLE'
            for j in range(i, i + k):
                s[j] = not s[j]
            flips += 1
    return flips


def main():
    with open(IN) as fin, open(OUT, 'w') as fout:
        t = int(fin.readline().strip())
        for i in range(t):
            s, k = fin.readline().split()
            k = int(k)
            res = run(s, k)
            print('Case #{}: {}'.format(i + 1, res), file=fout)


if __name__ == '__main__':
    main()

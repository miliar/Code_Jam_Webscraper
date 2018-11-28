#!/usr/bin/env python3

TEST = 'large'
IN = 'B-{}.in'.format(TEST)
OUT = 'B-{}.out'.format(TEST)


def run(n):
    digs = list(map(int, str(n)))
    while True:
        for i, d in enumerate(digs[:-1]):
            if d > digs[i + 1]:
                digs[i] = d - 1
                for j in range(i + 1, len(digs)):
                    digs[j] = 9
                break
        else:
            break
    return int(''.join(map(str, digs)))


def main():
    with open(IN) as fin, open(OUT, 'w') as fout:
        t = int(fin.readline().strip())
        for i in range(t):
            n = int(fin.readline().strip())
            res = run(n)
            print('Case #{}: {}'.format(i + 1, res), file=fout)


if __name__ == '__main__':
    main()

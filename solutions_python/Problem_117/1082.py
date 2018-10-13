#!/usr/bin/env python3
import sys


def solve(data):
    N, M, grass = data
    hmax = [-sys.maxsize] * N
    vmax = [-sys.maxsize] * M
    for i, row in enumerate(grass):
        for j, val in enumerate(row):
            hmax[i] = max(hmax[i], val)
            vmax[j] = max(vmax[j], val)
    for i, row in enumerate(grass):
        for j, val in enumerate(row):
            if hmax[i] > val and vmax[j] > val:
                return 'NO'
    return 'YES'


def read(fin):
    N, M = map(int, fin.readline().split())
    ar = []
    for i in range(N):
        ar.append(list(map(int, fin.readline().split())))
    return N, M, ar


def main():
    try:
        fin = open(sys.argv[1])
        if len(sys.argv) >= 3:
            fout = open(sys.argv[2], 'w')
        else:
            fout = sys.stdout
    except IndexError:
        print('Not enough command line options')
        sys.exit(1)
    except IOError as e:
        print(e)
        sys.exit(2)

    T = int(fin.readline())
    for t in range(T):
        data = read(fin)
        print('Case #{}: {}'.format(t + 1, solve(data)), file=fout)


if __name__ == '__main__':
    main()

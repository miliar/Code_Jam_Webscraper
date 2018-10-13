#!/usr/bin/python3

import sys

def solve(x, files):
    big = []
    small = []
    for f in files:
        if f > x // 2:
            big.append(f)
        else:
            small.append(f)

    big.sort(reverse=True)
    small.sort()

    pih = 0
    bi = 0
    si = 0
    while bi < len(big) and si < len(small):
        if big[bi] + small[si] <= x:
            pih += 1
            bi += 1
            si += 1
        else:
            bi += 1

    return len(big) + ((len(small) - pih) + 1) // 2

def main():
    T = int(next(sys.stdin))
    for t in range(1, T+1):
        n, x = map(int, next(sys.stdin).split())
        files = map(int, next(sys.stdin).split())
        print("Case #{}: {}".format(t, solve(x, files)))

if __name__ == '__main__':
    main()


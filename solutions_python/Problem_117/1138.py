#!/usr/bin/env python3

def calc(grid):
    rmax = [max(row) for row in grid]
    cmax = [max(col) for col in zip(*grid)]
    return rmax, cmax

def judge(grid):
    rmax, cmax = calc(grid)
    for j, row in enumerate(grid):
        for i, cell in enumerate(row):
            if min(rmax[j], cmax[i]) > cell:
                return False
    return True

def read():
    n = int(input())
    for counter in range(n):
        n_rows, n_cols = map(int, input().split())
        yield [list(map(int, input().split())) for j in range(n_rows)]

def main():
    for i, grid in enumerate(read(), 1):
        result = 'YES' if judge(grid) else 'NO'
        print('Case #{0}: {1}'.format(i, result))

if __name__ == '__main__':
    main()

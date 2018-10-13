#!/usr/bin/python3

import itertools

def is_mowing_allowed(height, current, target):
    new = [min(x, height) for x in current]

    return all(map(lambda x: x[0] >= x[1], zip(new, target)))

def needs_mowing(current, target):
    return any(map(lambda x: x[0] > x[1], zip(current, target)))

def mow_row(rows, row_no, height):
    rows[row_no] = [min(x, height) for x in rows[row_no]]

def mow_col(rows, col_no, height):
    for r in rows:
        r[col_no] = min(r[col_no], height)

def get_col(rows, col_no):
    return [x[col_no] for x in rows]

def is_possible(M, N, rows):
    lh = [x for x in sorted(set(sum(rows, [])))]

    lawn = list()
    for _ in range(N):
        lawn.append(list(itertools.repeat(100, M)))

    for i in range(N):
        if needs_mowing(lawn[i], rows[i]):
            for h in reversed(lh):
                if is_mowing_allowed(h, lawn[i], rows[i]):
                    mow_row(lawn, i, h)

    for j in range(M):
        lawn_col = get_col(lawn, j)
        target_col = get_col(rows, j)
        if needs_mowing(lawn_col, target_col):
            for h in reversed(lh):
                if is_mowing_allowed(h, lawn_col, target_col):
                    mow_col(lawn, j, h)

    for i in range(N):
        if lawn[i] != rows[i]:
            return 'NO'

    return 'YES'

def main():
    no_test_cases = int(input())

    for i in range(1, no_test_cases + 1):
        N, M = map(int, input().split())

        rows = list()

        for y in range(N):
            rows.append([x for x in map(int, input().split())])

        print('Case #{0}: {1}'.format(i, is_possible(M, N, rows)))

if __name__ == '__main__':
    main()

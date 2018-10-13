# coding: utf-8

import sys

def test_horizontal(rows):
    # horizontal check
    is_possible = []
    for row in rows:
        m = max(row)
        is_possible.append([m == h for h in row])
    return is_possible

def test_vertical(rows):
    # vertical check
    is_possible = []
    for col in zip(*rows):
        m = max(col)
        is_possible.append([m == h for h in col])
    return zip(*is_possible)

def solve(N, M, rows):
    check1 = test_horizontal(rows)
    check2 = test_vertical(rows)
    for n in range(N):
        for m in range(M):
            if not (check1[n][m] or check2[n][m]):
                return 'NO'

    return 'YES'

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = list(reversed(f.read().split('\n')))
        T = int(lines.pop())
        for t in range(T):
            N, M = map(int, lines.pop().split())
            result = solve(N, M, [map(int, lines.pop().split()) for i in range(N)])
            print 'Case #{}: {}'.format(t + 1, result)


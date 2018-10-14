import sys
from collections import defaultdict
from itertools import permutations

# sys.stdin = open('b1.in')
sys.stdin = open('B-small-attempt0.in')
# sys.stdin = open('B-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it(n, p, r, q):
    res = 0
    if n == 1:
        for j in range(p):
            i_min = 10 * q[0][j] // (11 * r[0])
            if 10 * q[0][j] % (11 * r[0]) > 0:
                i_min += 1
            i_max = 10 * q[0][j] // (9 * r[0])
            if i_min <= i_max:
                res += 1
    if n == 2:
        for perm in permutations(range(p)):
            resp = 0
            for j in range(p):
                i_min0 = 10 * q[0][j] // (11 * r[0])
                if 10 * q[0][j] % (11 * r[0]) > 0:
                    i_min0 += 1
                i_min1 = 10 * q[1][perm[j]] // (11 * r[1])
                if 10 * q[1][perm[j]] % (11 * r[1]) > 0:
                    i_min1 += 1
                i_max0 = 10 * q[0][j] // (9 * r[0])
                i_max1 = 10 * q[1][perm[j]] // (9 * r[1])
                i_min = max(i_min0, i_min1)
                i_max = min(i_max0, i_max1)
                if i_min <= i_max:
                    resp += 1
            if resp > res:
                res = resp
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        n, p = map(int, input().split())
        r = list(map(int, input().split()))
        q = [list(map(int, input().split())) for _ in range(n)]
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it(n, p, r, q)
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()

import sys
from collections import defaultdict

# sys.stdin = open('a1.in')
# sys.stdin = open('A-small-attempt0.in')
sys.stdin = open('A-large.in')
sys.stdout = open('out.txt', 'w')


def solve_it(s, k):
    a = [int(l == '+') for l in s]
    n = len(s)
    res = 0
    for i in range(n - k + 1):
        if a[i] == 0:
            res += 1
            for j in range(i, i + k):
                a[j] = 1 - a[j]
    ok = True
    for i in range(n):
        ok &= a[i] ==1
    if not ok:
        return "IMPOSSIBLE"
    return res


def main():
    n_cases = int(input())
    for test_case in range(1, n_cases + 1):
        s, k = input().split()
        k = int(k)
        print(test_case, file=sys.stderr, end=' ')
        res = solve_it(s, k)
        print('Case #' + str(test_case) + ':', res)

    print(file=sys.stderr)


if __name__ == '__main__':
    main()

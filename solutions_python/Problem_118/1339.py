import sys
import gmpy
import math


def msg(pos, s):
    print('Case #{0}: {1}'.format(pos, s))


def is_num_palindrome(x):
    s = str(x)
    n = len(s)
    for i in range(n / 2):
        if s[i] != s[n - i - 1]:
            return False

    return True


def win(x):
    if is_num_palindrome(x):
        root, _ = gmpy.mpz(x).root(2)
        if root * root == x:
            if is_num_palindrome(root):
                return True

    return False


def solve_range(lo, hi):
    count = 0

    for i in xrange(lo, hi + 1):
        if win(i):
            count += 1

    return count


def solve(filename):
    with open(filename) as f:
        N = int(f.readline().strip())

        for i in range(N):
            a, b = map(int, f.readline().strip().split(' '))
            count = solve_range(a, b)
            msg(i + 1, count)

if __name__ == '__main__':
    solve(sys.argv[1])


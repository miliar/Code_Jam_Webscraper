#! /usr/bin/env python

from sys import stdin


debug = False

def debug_print(s):
    if debug:
        print('    DEBUG: {}'.format(s))


def gen_palindrome(start, stop):
    str_start = str(start)
    n = len(str_start)
    while True:
        d, r = divmod(n, 2)
        x = 10**(d+r-1)
        end = x * 10
        while x < end:
            s = str(x)
            if r == 1:
                p = int(s + s[::-1][1:])
            else:
                p = int(s + s[::-1])
            if p > stop:
                return
            if p >= start:
                yield p
            x += 1
        n += 1

g = gen_palindrome


def is_palindrome(x):
    s = str(x)
    r = s[::-1]
    return s == r


def square_root(x):
    a, b = divmod(x.bit_length(), 2)
    r = 2 ** (a + b)
    while True:
        y = (r + x // r) // 2
        if y >= r:
            break
        r = y
    return r


def is_fair_and_square(x):
    if not(is_palindrome(x)):
        return False
    r = int(square_root(x))
    return r * r == x and is_palindrome(r)


def is_root_fair_and_square(x):
    return is_palindrome(x) and is_palindrome(x*x)


if __name__ == '__main__':
    num_cases = int(stdin.readline().strip())

    for case in range(num_cases):
        A, B = [int(x) for x in stdin.readline().strip().split()]
        debug_print('A: {}    B: {}'.format(A, B))

        count = 0
        #x = A
        #while x <= B:
            #if is_fair_and_square(x):
        for x in gen_palindrome(square_root(A), square_root(B)):
            if x*x >= A and x*x <= B and is_root_fair_and_square(x):
                count += 1
                debug_print('{} {}'.format(x*x, x))

        out = count
        print('Case #{}: {}'.format(case+1, out))



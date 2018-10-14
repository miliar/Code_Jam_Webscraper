#! /usr/bin/env python3

from functools import lru_cache


@lru_cache(maxsize=None)
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def is_my_square_fair_and_square(num):
    # special case
    if num == 3:
        return True
    # optimization since starting with 3, 4, 5, 6, 7, 8, 9
    # makes your square not a palindrome
    if str(num)[0] not in "12":
        return False
    return is_palindrome(num) and is_palindrome(num ** 2)

fair_and_squares = [x ** 2 for x in range(1, 10 ** 7)
                    if is_my_square_fair_and_square(x)]

T = int(input())
for case in range(T):
    A, B = [int(x) for x in input().split()]
    answer = len(list(filter(lambda x: A <= x <= B, fair_and_squares)))
    print("Case #{0}: {1}".format(case + 1, answer))

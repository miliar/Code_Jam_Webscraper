# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser
import math

# Input
#
# 3
# 1 4
# 10 120
# 100 1000
#
# Output
#
# Case #1: 2
# Case #2: 0
# Case #3: 2


def is_palindrome(num):
    return str(num) == str(num)[::-1]


def myxrange(start, stop):
    step = 1
    while start < stop:
        yield start
        start += step


def construct_palindrome(num, sym):
    string = str(num)
    if sym:
        return int(string + string[::-1])
    else:
        return int(string + string[:-1][::-1])


def get_half(num):
    # split in two halfs to find first suitable palindrome
    string = str(num)
    symmetry = 1 - len(string) % 2
    half_or_less = len(string) / 2
    half_or_more = half_or_less + len(string) % 2
    # print half_or_less, half_or_more, start_array[:half_or_less], start_array[half_or_more:][::-1]
    first_half = int(string[:half_or_more])
    second_half = int(string[half_or_less:][::-1])
    # print half_or_less, half_or_more, first_half, second_half
    if first_half == second_half:
        return first_half, 1, symmetry
    return first_half + int(first_half < second_half), 0, symmetry


def solve(*lines):
    a, b = map(int, lines)
    # print a, b
    start = int(math.ceil(math.sqrt(a)))
    max_half, eq, symmetry = get_half(start)
    start_val = int(max_half)

    finish = int(math.floor(math.sqrt(b)))
    # oops, leading zero expected:
    if finish % 10 == 0:
        finish -= 1
    max_half, eq, finish_symmetry = get_half(finish)
    finish_val = int(max_half)
    if not eq:
        finish_val -= 1
    # return start_val, finish_val
    # print start, finish, symmetry, finish_symmetry
    # print 'start-stop:', start_val, finish_val, symmetry, finish_symmetry
    count = 0
    val = start_val
    val_len = len(str(val))
    # workaround for close ranges
    if symmetry == finish_symmetry and val > finish_val:
        return 0
    while 1:
        # print val, symmetry, finish_symmetry
        palindrome = construct_palindrome(val, symmetry)
        if is_palindrome(palindrome * palindrome):
            # print palindrome, palindrome * palindrome
            count += 1
        val += 1
        new_val_len = len(str(val))
        if symmetry == finish_symmetry and val > finish_val:
            break
        if val_len < new_val_len:
            if symmetry == 0:
                symmetry = 1
                val /= 10
            else:
                symmetry = 0
                val_len = new_val_len
    return count

@iter_parser
def parse(nxtline):
    return nxtline().split()


if __name__ == "__main__":
    from codejam import CodeJam
    # import ipdb; ipdb.set_trace()
    CodeJam(parse, solve).main()

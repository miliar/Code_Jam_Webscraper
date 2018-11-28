#!python
from __future__ import print_function

import sys
from bisect import *

# maximum number of digits in the root of fair and square palindrome
#MAX_ROOT_DIGITS = 52
MAX_ROOT_DIGITS = 52
DIGITS = '0123456789'

FOUND_NUMBERS = []
ROOTS = []

#optimization:
DIGITS = '012'
FOUND_NUMBERS = [9]
ROOTS = [3]


def is_pal(s):
    l = len(s)
    for i in range(l // 2):
        if s[i] != s[l-1-i]:
            return False
    return True

def square_and_check(num):
    global FOUND_NUMBERS
    n = str(num**2)
    # note n can not start with '0', so it is ok
    if is_pal(n):
        FOUND_NUMBERS.append(int(n))
        ROOTS.append(num)
        return True
    return False

def check_num(str_num):
    if len(str_num) > MAX_ROOT_DIGITS:
        return
    if str_num.startswith('0'):
        deeper = True
    else:
        deeper = square_and_check(int(str_num))

    if deeper:
        for d in DIGITS:
            check_num(d + str_num + d)

def enumerate_pals():
    for d in DIGITS:
        check_num(d)
        check_num(d + d)

def result(a, b):
    assert(b>=a)
    i = bisect_left(FOUND_NUMBERS, a)
    j = bisect_right(FOUND_NUMBERS, b)
    return j - i

if __name__ == '__main__':
    enumerate_pals()
    FOUND_NUMBERS.sort()
    #print(str(FOUND_NUMBERS), file=sys.stderr)
    ROOTS.sort()
    #print(str(ROOTS))

    T = int(sys.stdin.readline().strip())
    #print('T:', repr(T))
    for t in range(T):
        a, b = [int(x) for x in sys.stdin.readline().strip().split(' ')]
        print("Case #{}: {}".format(str(t+1), result(a, b)))


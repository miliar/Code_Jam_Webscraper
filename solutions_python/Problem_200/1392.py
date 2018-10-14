#!/usr/bin/env pypy3
"""Task #2"""


def check(num, last, good, bad):

    if num == 0:
        return good
    current = num % 10
    if current <= last:
        good = str(current) + good
        bad = '9' + bad
    else:
        good = bad
        current -= 1
        good = str(current) + good
        bad = '9' + bad

    return check(num // 10, current, good, bad)


for case in range(1, int(input()) + 1):

    num = int(input())
    res = check(num, 10, '', '')
    if res[0] == '0':
        res = res[1:]

    print('Case #{}: {}'.format(str(case), res))

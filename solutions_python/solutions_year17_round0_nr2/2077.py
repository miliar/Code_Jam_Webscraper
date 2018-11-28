# coding=utf-8

# Created on 08/04/2017
# Code Jam 2017 qr b
# @author: manolo

import sys

ifile = sys.stdin
ofile = sys.stdout


def r():
    return ifile.readline()[:-1]


def w(case, what):
    ofile.write('Case #{}: {}\n'.format(case, what))


def solve(numbers, last_ok):

    # print
    # print '------------'
    # print numbers
    # print 'last ok: {} [{}]'.format(numbers[last_ok], last_ok)
    # print '------------'

    last = numbers[last_ok]
    for i in range(last_ok+1, len(numbers)):
        c = numbers[i]
        # print 'last: {}'.format(last)
        # print 'current: {}'.format(c)
        # if last <= c: everything ok!
        if c < last:
            if c == 0:
                numbers[i-1] = last - 1
                for j in range(i, len(numbers)):
                    numbers[j] = 9
                # print 'current is 0'
                # print 'changed number at [{}]: {} -> {}'.format(i-1, numbers[i-1]+1, numbers[i-1])
                # print 'changed all numbers from [{}] to 9: {}'.format(i, numbers)
                return solve(numbers, i-2 if i > 1 else 0)
            else:
                numbers[i] = c - 1
                for j in range(i+1, len(numbers)):
                    numbers[j] = 9
                # print 'changed number at [{}]: {} -> {}'.format(i, numbers[i]+1, numbers[i])
                # print 'changed all numbers from [{}] to 9: {}'.format(i+1, numbers)
                return solve(numbers, i-1)
        last = c

    return int(''.join([str(c) for c in numbers]))

T = int(r())
for case in range(1, T+1):
    s = r()
    # print '#################################################'
    what = solve([int(n) for n in s], 0)
    w(case, what)
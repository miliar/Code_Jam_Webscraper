# coding: utf8

import sys
import re


def flip_char(character):
    if character == '+':
        return '-'
    elif character == '-':
        return '+'
    else:
        raise ValueError(character)


def flip(string):
    return ''.join(flip_char(x) for x in string)


def is_tidy(num):
    tmp = str(num)
    return all(tmp[i] <= tmp[i + 1] for i in range(len(tmp) - 1))


def tidify_last_one(num):
    tmp = re.sub('(.)(9*)$', r'|9\g<2>', str(num))
    tmp = str(int(tmp.split('|')[0]) - 1) + tmp.split('|')[1]
    return int(tmp)


def tidify(num):
    while not is_tidy(num):
        num = tidify_last_one(num)
    return num


def main():
    T = int(sys.stdin.readline())
    for _T in range(T):
        N = int(sys.stdin.readline())
        result = tidify(N)
        print('Case #%s: %s' % (_T + 1, result))


if __name__ == '__main__':
    main()

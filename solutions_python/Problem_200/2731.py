#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def is_tidy(i):
    last = 9
    while 0 < i:
        d = i % 10
        if last < d:
            return False
        else:
            last = d
        i = i // 10
    return True


def main():
    for case in range(int(sys.stdin.readline().strip())):
        n = int(sys.stdin.readline().strip())
        while True:
            if is_tidy(n):
                print('Case #{}: {}'.format(case + 1, n))
                break
            else:
                n -= 1


if __name__ == '__main__':
    main()

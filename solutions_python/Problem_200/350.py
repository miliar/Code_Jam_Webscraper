#!/usr/bin/python
# -*- coding utf-8 -*-


def solve():
    n = int(input())
    st = 1
    for i in range(20):
        st2 = st * 10
        if n // st % 10 < n // st2 % 10:
            n = n // st2 * st2 - 1
        st = st2
    return n


def main():
    t = int(input())
    for i in range(t):
        print('Case #%d:' % (i+1), solve())


if __name__ == '__main__':
    main()

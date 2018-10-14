#!/usr/bin/env python

import sys


def time_get_cookie(c, f, x):
    c = float(c)
    f = float(f)
    x = float(x)

    n_cookie_per_sec = 2
    r_time = 0
    min_time = x / n_cookie_per_sec

    while 1:
        r_time += c / n_cookie_per_sec
        n_cookie_per_sec += f
        t_time = r_time + x / n_cookie_per_sec

        if t_time < min_time:
            min_time = t_time
        else:
            return min_time


def main():
    with open(sys.argv[1], 'r') as fi:
        n_case = int(fi.readline())

        r_case = 0
        while r_case < n_case:
            r_case += 1

            c, f, x = [float(i) for i in fi.readline().split(' ')]
            result = time_get_cookie(c, f, x)
            print('Case #{0}: {1:.7f}'.format(r_case, result))

if __name__ == '__main__':
    main()

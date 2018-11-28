from __future__ import division

from math import floor, ceil

# f_name = 'sample.in'
# f_name = 'C-small-1-attempt0.in'
f_name = 'C-small-1-attempt1.in'
# f_name = 'B-large.in'


def parse_input(str_test):
    t = str_test.split()
    n = map(int, t)
    return n


def solve(test):
    n = test[0]
    k = test[1]
    # if k == n:
    #     return '0 0'
    # if k > n / 2:
    #     return '1 0'

    s = [n]
    ind = 0
    v = n

    for i in range(k):
        (l, r) = floor((v - 1) / 2), ceil((v - 1) / 2)
        s[ind] = r
        s.insert(ind, l)

        v = max(s)
        ind = s.index(v)

    var = map(int, [max(r, l), min(r,l)])
    return ' '.join(map (str, var))

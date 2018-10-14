#!/usr/bin/python
#
# author: tzeng.yuxio@gmail.com
# usage: cat file.input | ./qround-problem-a.py > file.output

import sys

def solve():
    s = sys.stdin.readline()[:-1]
    c, f, x = [float(x) for x in s.split()]
    min_t = x / 2
    pass_t = 0
    num_farm = 0
    while pass_t < min_t:
        prod = 2 + num_farm * f # production
        pass_t += (c / prod)
        num_farm += 1
        this_t = pass_t + (x / (prod + f))
        min_t = min(min_t, this_t)

    return repr(round(min_t, 7))

t = (int)(sys.stdin.readline())
for i in range(t):
    print 'Case #' + repr(i+1) + ': ' + solve()

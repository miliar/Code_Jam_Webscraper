__author__ = 'deniskrut'

# https://code.google.com/codejam/contest/2994486/dashboard#s=p1

import sys

t_num = int(sys.stdin.readline())

for i in range(0, t_num):
    a, b, k = [int(x) for x in sys.stdin.readline().split()]

    res = 0
    for a_opt in range(0, a):
        for b_opt in range(0, b):
            if a_opt&b_opt < k:
                res += 1

    print "Case #" + str(i + 1) + ": " + str(res)
import sys
import math

t = int(sys.stdin.readline())
for t0 in range(t):
    d, n = sys.stdin.readline().split(' ')
    d, n = int(d), int(n)
    ki = []
    si = []
    for n0 in range(n):
        k, s = sys.stdin.readline().split(' ')
        k, s = int(k), int(s)
        ki.append(k)
        si.append(s)

    max_t_so_far = 0.
    for i in range(0,n):
        t = (d - ki[i])/si[i]
        max_t_so_far = max(t, max_t_so_far)
    res = d/max_t_so_far
    print("Case #", t0 + 1, ": ", res, sep = '')
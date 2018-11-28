
from math import pi

def a_side(r_h):
    r, h = r_h
    return 2 * pi * r * h

def a_top(r_h):
    r, _ = r_h
    return pi * r * r

def a_tot(r_h):
    return a_top(r_h) + a_side(r_h)

def contrib(rh, rad):
    c = a_side(rh)
    if rh[0] > rad:
        c += a_top(rh) - pi * rad * rad
    return c

def find_max(r_hs, rad):
    max_i = 0
    mx = contrib(r_hs[0], rad)
    for i, rh in enumerate(r_hs):
        v = contrib(rh, rad)
        if v > mx:
            mx = v
            max_i = i
    return max_i

def solve(n, k, r_hs):
    assert k <= n
    rad = 0
    s = 0.0
    for i in range(k):
        m = find_max(r_hs, rad)
        s += a_side(r_hs[m])
        rad = max(rad, r_hs[m][0])
        del r_hs[m]
    return s + rad * rad * pi

t = int(input())
for i in range(1, t + 1):
    n, k = [int(c) for c in input().split(" ")]
    cakes = []
    for j in range(n):
        cakes.append(tuple([int(c) for c in input().split(" ")]))
    print("Case #{}: {}".format(i, solve(n, k, cakes)))

#!/usr/bin/python3


def solve(i):
    sn, sv, sx = input().split()
    n = int(sn)
    v = float(sv)
    x = float(sx)
    if n == 1:
        r, c = map(float, input().split())
        print("Case #", i, ": ", sep="", end="")
        if abs(c - x) > 1e-7:
            print("IMPOSSIBLE")
        else:
            print("%.20f" % (v / r))
    else:
        r0, c0 = map(float, input().split())
        r1, c1 = map(float, input().split())
        print("Case #", i, ": ", sep="", end="")
        if c0 == c1:
            c = c0
            r = r0 + r1
            if abs(c - x) > 1e-7:
                print("IMPOSSIBLE")
            else:
                print("%.20f" % (v / r))
            return 0
        if c0 < c1:
            r0, r1 = r1, r0
            c0, c1 = c1, c0
        if c1 > x or c0 < x:
            print("IMPOSSIBLE")
        else:
            t0 = (v * (x - c1)) / (r0 * (c0 - c1))
            t1 = (v - t0 * r0) / r1
            print("%.20f" % (max(t0, t1)))


t = int(input())
for i in range(t):
    solve(i + 1)

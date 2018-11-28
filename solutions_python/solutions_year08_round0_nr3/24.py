
import math

def FlySwatter():
    f, R, t, r, g = map(float, raw_input().split())
    p = g + 2.0 * r
    a = max(0.0, g - 2.0 * f)
    R1 = max(0.0, R - t - f)
    xn = int(R1 / p) + 1
    nn = 50000 / xn
    dx = a / nn
    isum = 0
    fsum = 0.0
    for xi in range(xn):
        x = xi * p + r + f + 0.5 * dx
        for i in range(nn):
            if x < R1:
                y = math.sqrt(R1 * R1 - x * x)
                yn = int(y / p)
                if yn:
                    isum += yn
                    y -= yn * p
                y -= (r + f)
                if y > 0.0:
                    fsum += min(y, a)
            x += dx
    area = math.pi * R * R
    hit = max(0.0, area - 4.0 * dx * (isum * a + fsum))
    print "%.7f" % (hit / area)

N = int(raw_input())
for testcase in range(N):
    print "Case #%d:" % (testcase + 1),
    FlySwatter()

import sys

N = input()
for i in range(1, N + 1):
    x = raw_input().split(' ')
    s, t, f, ds, g = 2.0, 0.0, float(x[0]), float(x[1]), float(x[2])
    while ds * (g - f) > s * f:
        t += f / s
        s += ds
    print 'Case #{0}: {1}'.format(i, t + g / s)

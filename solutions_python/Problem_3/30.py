from sys import stdin
from math import pi, sqrt, asin, acos

PRECISION = 1e-6

N = int(stdin.readline().strip())

def print_result(case, result):
    print 'Case #%d: %.6f' % (case, result)

def partial_disk_area(R, x, y):
    R2 = R**2
    assert(x >= 0 and y >= 0 and x**2 + y**2 <= R2)
    phi1 = asin(y / R)
    phi2 = acos(x / R)
    A1 = (phi2 - phi1) * R2 / 2
    A2 = (sqrt(R2-x**2) - y) * x / 2
    A3 = (sqrt(R2-y**2) - x) * y / 2
    return A1 - A2 - A3

for n in range(N):
    f, R, t, r, g = [float(x) for x in stdin.readline().strip().split()]
    a = g - 2 * f
    if a <= 0:
        print 'Case #%d: %.6f' % (n+1, 1)
        continue
    a2 = a**2
    Q = R - t - f
    Q2 = Q**2
    area = 0.0
    k = int(Q / (g + 2 * r) + 1)
    v1 = [i * g + (2*i+1) * r + f for i in range(k)]
    v2 = [x + a for x in v1]
    for i in range(k):
        x1 = v1[i]
        x2 = v2[i]
        for j in range(k):
            y1 = v1[j]
            y2 = v2[j]
            if x1**2 + y1**2 > Q2:
                # The whole square is outside
                pass
            elif x2**2 + y2**2 < Q2:
                # The whole square is inside
                area += a2
            else:
                # The square is partially inside
                area += partial_disk_area(Q, x1, y1)
                if sqrt(Q2-x1**2) > y2:
                    area -= partial_disk_area(Q, x1, y2)
                if sqrt(Q2-y1**2) > x2:
                    area -= partial_disk_area(Q, x2, y1)
    print 'Case #%d: %.6f' % (n+1, 1 - 4 * area / (R**2 * pi))

import sys

from numpy import array
from numpy.linalg import norm, solve, LinAlgError

input = sys.stdin
#input = open('B-sample.in')
T = int(input.readline().strip())

def input_case(input):
    flies = []
    N = int(input.readline().strip())
    for i in range(N):
        flies.append(map(float, input.readline().split()))

    return flies

def count_dmin_tmin(case):
    n = float(len(case))

    arr = array(case)
    s = sum(arr)/n
    r0 = s[:3]
    x0,y0,z0=r0
    v = s[3:]
    vx,vy,vz=v

    den = (vx ** 2 + vy **2 + vz **2)
    if den > 1e-9:
        a = array([[vy, -vx, 0],
                   [vz, 0, -vx],
                   [vx, vy, vz]])
        b = array([x0*vy-y0*vx, x0*vz-z0*vx, 0])
        s = solve(a, b)
        t = (s[0]-x0)/vx
    else:
        t=0

    if t<=0:
        t=0

    dmin = norm(r0 + v*t)

    return dmin, t


def process_case(case, i):
    dmin, tmin = count_dmin_tmin(case)
    print "Case #%d: %f %f" % (i + 1, dmin, tmin)

for i in xrange(T):
    process_case(input_case(input), i)


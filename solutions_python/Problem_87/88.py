import sys
import re
from math import *
from cmath import *


T = int(sys.stdin.readline())

for Case in range(T):
    ss = [int(s) for s in sys.stdin.readline()[:-1].split()]
    X = ss[0]
    S = ss[1]
    R = ss[2]
    t = ss[3]
    N = ss[4]
    roads = {0: 0}
    previous = 0
    for i in range(N):
        ss = [int(s) for s in sys.stdin.readline()[:-1].split()]
        B = ss[0]
        E = ss[1]
        W = ss[2]
        if W in roads:
            roads[W] += E - B
        else:
            roads[W] = E - B
        roads[0] += B - previous
        previous = E
    roads[0] += X - previous

    s = t
    time = 0
    for (W, L) in sorted(roads.items()):
        if (W + R) * s >= L:
            s -= L / (W + R)
            time += L / (W + R)
        else:
            time += (s + (L - (W + R) * s) / (W + S))
            s = 0
    print('Case #{0}: {1}'.format(Case + 1, time))


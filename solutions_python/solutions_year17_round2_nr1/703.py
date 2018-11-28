import sys
import os
import math
from itertools import product
from copy import deepcopy
from collections import defaultdict

def solve(D, horses):
    etas = [1. * (D - k) / s  for (k, s) in horses]
    return D / max(etas)


def line():
    return sys.stdin.readline().strip()

def write_solution(i, ans):
    sys.stdout.write(
        'Case #%s: %s\n' % (i, ans)
    )

if __name__ == '__main__':
    count = int(line())

    for i in range(count):
        D, N = line().split()

        horses = []
        for j in range(int(N)):
            K, S = line().split()
            horses.append((int(K), int(S)))
        write_solution(i + 1, solve(int(D), horses))
        



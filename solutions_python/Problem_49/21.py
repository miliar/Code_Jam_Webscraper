from sys import stdin, stdout
from math import *

C = int(stdin.readline().strip())
for i in range(C):
    N = int(stdin.readline().strip())
    plants = []
    for j in range(N):
        fields = stdin.readline().split()
        X = int(fields[0])
        Y = int(fields[1])
        R = int(fields[2])
        plants.append((X, Y, R))
    if N == 1:
        R = float(plants[0][2])
    elif N == 2:
        R = float(max(plants[0][2], plants[1][2]))
    elif N == 3:
        R = None
        for j in range(3):
            R1 = plants[j][2]
            R2 = (hypot(plants[(j + 1) % 3][0] - plants[(j + 2) % 3][0],
                        plants[(j + 1) % 3][1] - plants[(j + 2) % 3][1])
                      + plants[(j + 1) % 3][2] + plants[(j + 2) % 3][2]) / 2
            R0 = max(R1, R2)
            if R is None or R0 < R:
                R = R0
    else:
        R = 0.0
    stdout.write('Case #%d: %0.6f\n' % (i + 1, R))

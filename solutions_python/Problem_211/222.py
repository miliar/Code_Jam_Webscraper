#!/usr/bin/python

import sys
from operator import mul

def main(argv):
    inputFile = argv[0]
    f = open(inputFile, 'r')
    T = int(f.readline())
    for i in range(1, T+1):
        line = f.readline()[:-1]
        N, K = [int(k) for k in line.split(' ')]
        line = f.readline()[:-1]
        U = float(line)
        line = f.readline()[:-1]
        P = [float(k) for k in line.split(' ')]
        P.append(1.0)
        P.sort()
        print("Case #%r: %.8f" % (i, solve(N, K, U, P)))

def solve(N, K, U, P):
    index = 0
    while U > 1e-6:
        zyede = 0
        if U >= (index+1)*(P[index+1] - P[index]):
            zyede = P[index+1] - P[index]
        else:
            zyede = U/(index + 1)
        for i in range(0, index +1):
            P[i] += zyede
        U -= (index+1)*zyede
        index += 1

    return reduce(mul, P, 1)


if __name__ == '__main__':
    main(sys.argv[1:])


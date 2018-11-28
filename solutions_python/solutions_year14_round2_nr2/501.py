# coding=utf-8 *** gatopeich for Google Code Jam 2014

# Problem B. New Lottery Game

filename = 'B-small-attempt0'

import concurrent.futures
import numpy as np


def solve(case, A, B, K):
    print('#%d:' % case, A, B, K)

    if A<B: A,B = B,A

    As = np.arange(A)
    print(As)
    count = sum(np.sum((As&b) < K) for b in range(B))

    return case, count

if __name__ == '__main__':

    next_line = open(filename + '.in').readline
    out = open(filename + '.out', 'w')

    def write(*line):
        print(*line, file=out)
        print(*line)

    T = int(next_line())
    print(T, "cases")

    tests = []
    for case in range(1, T + 1):
        A,B,K = map(int,next_line().split())
        tests.append((case, A, B, K))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for solution in executor.map(solve, *zip(*tests)):
            write('Case #%d: %s' % solution)

    out.close()

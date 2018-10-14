# coding=utf-8 *** gatopeich for Google Code Jam 2014

# Problem A. The Repeater

import concurrent.futures
import numpy as np


def solve(case, strings):
    print('#%d:' % case, strings)

    items = []
    chars0 = None
    for s in strings:
        chars = ''
        counts = []
        last_c = None
        for c in s:
            if c != last_c:
                chars += c
                counts.append(1)
                last_c = c
            else:
                counts[-1] += 1
        print(chars, counts, s)
        if chars0:
            if chars != chars0:
                return case, "Fegla Won"
            A = np.vstack((A,counts))
        else:
            chars0 = chars
            A = np.array(counts)
    return case, int(abs(A-A.mean(0)).sum())

if __name__ == '__main__':

    filename = 'A-small-attempt0'

    next_line = open(filename + '.in').readline
    out = open(filename + '.out', 'w')

    def write(*line):
        print(*line, file=out)
        print(*line)

    T = int(next_line())
    print(T, "cases")

    tests = []
    for case in range(1, T + 1):
        N = int(next_line())
        strings = [next_line().rstrip() for _ in range(N)]
        tests.append((case, strings))

    with concurrent.futures.ProcessPoolExecutor() as executor:
        for solution in executor.map(solve, *zip(*tests)):
            write('Case #%d: %s' % solution)

    out.close()

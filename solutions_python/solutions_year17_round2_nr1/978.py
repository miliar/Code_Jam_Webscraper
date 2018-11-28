#! /usr/bin/env python3

import sys

def solve(problem):
    D, horses = problem
    eta = 0
    for (k, s) in reversed(horses):
        h = (D - k)
        h_eta = h / s
        eta = max(eta, h_eta)

    return '{:.6f}'.format(D / eta)

def parse(content):
    (T, *numbers) = map(int, content.split())
    for i in range(T):
        (D, n, *numbers) = numbers
        horses = list()
        for j in range(n):
            ki, si, *numbers = numbers
            horses.append((ki, si))
        yield (D, horses)


#################################################################

if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    with open(filename + '.out', 'w') as out:   
        for (i, case) in enumerate(parse(content), 1):
            result = solve(case)
            for o in (out, sys.stdout):
                print('Case #', i, ': ', result, sep='', file=o)

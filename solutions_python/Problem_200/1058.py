#! /usr/bin/env python3

import sys

def first_tidy(n, k):
    return int(str(n) * k)

def last_tidy(n, k):
    return int(str(n-1) + '9' * (k-1))

def solve(problem):
    result = list()

    k = len(problem)
    n = int(problem)

    for i in range(len(problem)):
        h = int(problem[i])

        if n < first_tidy(h, k):
            result.append(str(h-1))
            result.extend(['9'] * (k-1))
            break
        else:
            result.append(str(h))
            n = n - n // (10 ** (k-1)) * (10 ** (k-1))
        
        k = k - 1

    return int(''.join(result))

def parse(content):
    T, *cases = content.split('\n')
    return int(T), cases

#################################################################

if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    with open(filename + '.out', 'w') as out:   
        T, cases = parse(content)
        cases = cases[:T]
        for (i, case) in enumerate(cases, 1):
            result = solve(case)
            for o in (out, sys.stdout):
                print('Case #', i, ': ', result, sep='', file=o)

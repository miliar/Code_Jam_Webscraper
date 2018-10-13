#! /usr/bin/env python3

import sys
import re

D = {'+': '-', '-': '+'}

def flip(s, k):
    return ''.join(map(D.get, s[:k])) + s[k:]

        
def solve(problem):
    s, k = problem

    count = 0
    while len(s) >= k:
        if s[0] == '-':
            s = flip(s, k)
            count += 1
        s = re.sub('^[+]*', '', s)

    if all(c == 1 for c in s):
        return str(count)
    else:
        return 'IMPOSSIBLE'

    return '{} {}'.format(*problem)

def parse(content):
    for line in content.split('\n')[1:]:
        s, k = line.split()
        yield(s, int(k))

#################################################################

if __name__ == '__main__':
    filename = sys.argv[1]

    with open(filename) as f:
        content = f.read().strip()

    for (i, case) in enumerate(parse(content), 1):
        result = solve(case)
        with open(filename + '.out', 'w') as out:   
            for o in (out, sys.stdout):
                print('Case #', i, ': ', result, sep='', file=o)

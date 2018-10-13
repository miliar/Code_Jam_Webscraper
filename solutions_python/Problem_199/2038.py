
import os
import sys
import logging
from pprint import pformat

log = logging.getLogger()
logging.basicConfig(level=logging.WARN)


def get_input():
    with open(sys.argv[1], 'r') as f:
        return f.readlines()[1:]


def is_solved(s):
    return '-' not in s


def solve(s, k):
    steps = set()
    n = 0
    sl = len(s)
    log.debug('Solve: {} {}'.format(s, k))
    while not is_solved(s):
        if s in steps:
            log.debug('REPEAT: {}'.format(s))
            log.debug(pformat(steps))
            return 'IMPOSSIBLE'
        else:
            steps.add(s)
        s = list(s)
        i = s.index('-')
        if sl - k < i:
            log.debug('IMP: {} | {} | {}'.format(s, sl, i))
            return 'IMPOSSIBLE'
        for j in range(i, i + k):
            s[j] = '-' if s[j] == '+' else '+'
        s = ''.join(s)
        n += 1
    return n


def main():
    lines = get_input()
    outputs = []
    for i, line in enumerate(lines):
        log.debug('CASE #{}'.format(i))
        s, k = line.split()
        k = int(k)
        n = solve(s, k)
        print('Case #{}: {}'.format(i+1, n))


if __name__ == '__main__':
    main()

#!/usr/bin/env python

import sys
from string import ascii_lowercase

def decode_example():
    result = {' ': ' '}
    for line in open('example'):
        their, our = line.split()
        assert len(their) == len(our)
        for t, o in zip(their, our):
            result[t] = o
    mk = set(ascii_lowercase) - set(result.keys())
    mv = set(ascii_lowercase) - set(result.values())
    if not mk and not mv:
        return result
    if len(mk) == len(mv) == 1:
        mke, = mk
        mve, = mv
        result[mke] = mve
        return result
    raise('dupa')

def solve(d):
    num = None
    for no, line in enumerate(sys.stdin):
        if num is None:
            num = int(line.strip())
            continue
        result = solve_line(line.strip(), d)
        print('Case #%d: %s' % (no, result))

def solve_line(line, d):
    return ''.join(d[c] for c in line)

def main():
    d = decode_example()
    solve(d)

if __name__ == '__main__':
    main()


#!/usr/bin/env python3 -u

import argparse
import itertools
import logging
import sys


def solve(state, size):
    try:
        size = int(size)
        if size > len(state):
            return 'IMPOSSIBLE'
        prev = set()
        for i in itertools.count():
            print('\r' + str(i), end='', flush=True, file=sys.stderr)
            if '-' in state:
                index = state.index('-')
                if index > len(state) - size:
                    return 'IMPOSSIBLE'
                state = state[:index] + flip(state[index:index+size]) + state[index+size:]
                if state in prev:
                    return 'IMPOSSIBLE'
                else:
                    prev.add(state)
                state = ''.join(reversed(state))
            else:
                return i
    finally:
        print('', file=sys.stderr)


def flip(state):
    return ''.join('-' if s is '+' else '+' for s in state)


def problems(path):
    f = open(path, 'r')
    count = int(f.readline())

    for i in range(count):
        line = f.readline()
        yield i+1, line.strip().split(' ', 1)


def format(i, solution):
    return f"Case #{i}: {solution}"


def main(argv=sys.argv[1:]):
    logging.basicConfig(level=logging.DEBUG)
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", '--debug', action='store_true')
    ap.add_argument('-i', '--index', type=int)
    ap.add_argument('input')
    args = ap.parse_args(argv)

    ps = problems(args.input)
    if args.index is not None:
        ps = itertools.islice(ps, args.index-1, args.index)

    for i, problem in ps:
        print("Problem #%d: %s" % (i, problem), file=sys.stderr)
        print(format(i, solve(*problem)))


if __name__ == '__main__':
    main()
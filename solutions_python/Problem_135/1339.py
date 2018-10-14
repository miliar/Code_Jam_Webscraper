#!/usr/bin/env python

import sys

def get_row(in_stream):
    idx = int(in_stream.next()) - 1
    grid = [in_stream.next().split() for _ in xrange(4)]
    return set(grid[idx])

def main(in_stream, out_stream):
    n_cases = int(in_stream.next())
    for i in xrange(1, n_cases+1):
        cards = get_row(in_stream)
        cards.intersection_update(get_row(in_stream))
        if len(cards) == 0:
            outcome = 'Volunteer cheated!'
        elif len(cards) == 1:
            outcome = cards.pop()
        else:
            outcome = 'Bad magician!'
        out_stream.write('Case #%d: %s\n' % (i, outcome))

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)

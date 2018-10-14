#!/usr/bin/env python
"""
Problem B. Lwanmower
Qualification Round 2013, Google Code Jam

13 April 2013

"""
import itertools
import logging
import sys


def setup_parser():
    from optparse import OptionParser
    usage = 'usage: %prog [options] <input file>'
    parser = OptionParser(usage=usage)
    parser.add_option('-v', '--verbose', dest='verbose', action='count',
                      help='increase verbosity')
    return parser


def setup_logging(options):
    log_level = logging.WARNING
    if options.verbose == 1:
        log_level = logging.INFO
    elif options.verbose >= 2:
        log_level = logging.DEBUG
    logging.basicConfig(level=log_level)


def check(lawn, i, j, height):
    nrows = len(lawn)
    ncols = len(lawn[0])

    n_col = sum([1 if e <= height else 0 for e in lawn[i]])
    t_lawn = [list(i) for i in zip(*lawn)]
    n_row = sum([1 if e <= height else 0 for e in t_lawn[j]])

    return n_col == ncols or n_row == nrows


def isPossible(lawn):
    possible = [[check(lawn, i, j, elem)
                 for j, elem in enumerate(row)]
                 for i, row in enumerate(lawn)]
    return all([all(p) for p in possible])


def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = setup_parser()
    options, args = parser.parse_args()
    setup_logging(options)

    if len(args) < 1:
        parser.print_help()
        return 2

    try:
        with open(args[0], 'r') as f:
            lines = [line.strip() for line in f.readlines()]
    except IOError, err:
        print >>sys.stderr, err
        return 1

    T = int(lines[0])
    i = 1
    for t in xrange(T):
        N, M = [int(n) for n in lines[i].split()]
        i += 1
        j = i + N
        lawn = [map(int, line.split()) for line in lines[i:j]]
        print 'Case #%d: %s' % (t + 1, 'YES' if isPossible(lawn) else 'NO')
        i = j

    return 0


if __name__ == '__main__':
    sys.exit(main())

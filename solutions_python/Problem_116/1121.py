#!/usr/bin/env python
"""
Problem A. Tic-Tac-Toe-Tomek
Qualification Round 2013, Google Code Jam

13 April 2013

"""
import itertools
import logging
import sys


nrows, ncols = 4, 4


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


def read_board(chars):
    return chars[:-1]


def transform(board):
    lrows = [list(row) for row in board]
    ltrans = [list(i) for i in zip(*lrows)]
    return [''.join(r) for r in ltrans]


def diagonal(board):
    lboard = [list(row) for row in board]
    dia1 = ''.join([r[i] for i, r in enumerate(lboard)])
    dia2 = ''.join([r[-i-1] for i, r in enumerate(lboard)])
    return [dia1, dia2]

def count(board, players):
    return [sum([row.count(p) for p in players]) for row in board]


def status(board):
    if nrows in count(board, ['X', 'T']):
        return 'X won'
    if nrows in count(board, ['O', 'T']):
        return 'O won'
    if nrows in count(transform(board), ['X', 'T']):
        return 'X won'
    if nrows in count(transform(board), ['O', 'T']):
        return 'O won'
    if nrows in count(diagonal(board), ['X', 'T']):
        return 'X won'
    if nrows in count(diagonal(board), ['O', 'T']):
        return 'O won'
    if sum(count(board, ['.'])) == 0:
        return 'Draw'
    return 'Game has not completed'


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

    t = int(lines.pop(0))
    for i in xrange(t):
        ith = (nrows + 1) * i
        board = read_board(lines[ith:ith+nrows+1])
        print 'Case #%d: %s' % (i + 1, status(board))

    return 0


if __name__ == '__main__':
    sys.exit(main())

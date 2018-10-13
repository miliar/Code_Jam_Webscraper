#!/usr/bin/env python
"""
Problem A. Password Problem
Round 1A 2012, Google Code Jam

28 April 2012

"""
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


def compute(a, b, probs):
    # Keystrokes if I press enter right away
    expected = [b+2]

    # Keystrokes if I press backspace i times
    for i in xrange(a):
        k = b - a + 2*i + 1
        m = b + 1
        p = prod(probs[:a-i])
        expected.append(k + m - m * p)

    return min(expected)


def prod(seq):
    def mul(x, y): return x*y
    return reduce(mul, seq)


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
        a, b = [int(x) for x in lines[i*2].split()]
        probs = [float(p) for p in lines[i*2+1].split()]
        print 'Case #%d: %.6f' % (i + 1, compute(a, b, probs))

    return 0


if __name__ == '__main__':
    sys.exit(main())

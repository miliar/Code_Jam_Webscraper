#!/usr/bin/env python
"""
Problem A. Speaking in Tongues
Qualification Round 2012, Google Code Jam

14 April 2012

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


def translate(msg):
    trans = {'a': 'y', 'b': 'h', 'c': 'e', 'd': 's', 'e': 'o', 'f': 'c',
             'g': 'v', 'h': 'x', 'i': 'd', 'j': 'u', 'k': 'i', 'l': 'g',
             'm': 'l', 'n': 'b', 'o': 'k', 'p': 'r', 'q': 'z', 'r': 't',
             's': 'n', 't': 'w', 'u': 'j', 'v': 'p', 'w': 'f', 'x': 'm',
             'y': 'a', 'z': 'q'}
    result = list(msg)
    for i in range(len(msg)):
        c = msg[i]
        if c in trans:
            result[i] = trans[c]
    return ''.join(result)


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
    for i in range(t):
        print 'Case #%d: %s' % (i + 1, translate(lines[i]))

    return 0


if __name__ == '__main__':
    sys.exit(main())

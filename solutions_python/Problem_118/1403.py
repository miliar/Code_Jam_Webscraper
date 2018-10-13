#!/usr/bin/env python
"""
Problem C. Fair and Square
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


def isPalindrome(word):
    return word == word[::-1]


def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y


def isFairSquare(n):
    square = isqrt(n)
    return square * square == n and isPalindrome(str(square))


def fair_square(a, b):
    count = 0
    for i in xrange(a, b+1):
        if isPalindrome(str(i)) and isFairSquare(i):
            count += 1
    return count


def fair_square2(a, b):
    palindromes = []
    for i in xrange(a, b+1):
        if isPalindrome(str(i)) and isFairSquare(i):
            palindromes.append(i)
    return palindromes


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
        a, b = [int(n) for n in lines[i].split()]
        print 'Case #%d: %d' % (t + 1, fair_square(a, b))
        #print 'Case #%d: %s' % (t + 1, fair_square2(a, b))
        i += 1

    return 0


if __name__ == '__main__':
    sys.exit(main())

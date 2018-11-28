"""
CodeJam 2013 Qualification round problem C fair and square
"""
import sys
from math import sqrt, ceil


def is_square(v):
    return ceil(sqrt(v)) == sqrt(v)


def is_palindrome(v):
    # convert number to string and check palindrome
    v = unicode(v)
    r = v[::-1]
    return v == r


def is_square_and_pal(v):
    text = unicode(v)
    if is_palindrome(text) and is_square(v):
        root = int(sqrt(v))
        return is_palindrome(root)
    return False


def solve(start, end):
    debug = False
    result = 0
    if debug: print('start={} end={}'.format(start, end))
    for i in xrange(start, end + 1):
        if is_square_and_pal(i) and is_palindrome(i):
            if debug: print('{} square and palindrome'.format(i))
            result += 1
        else:
            if debug: print('{} False'.format(i))

    return result


def main(argv=None):
    if argv is None:
        argv = sys.argv
    if len(argv) < 2:
        print(u'First argument is filename to read for test cases')
        return(1)
    infile = open(argv[1])
    num_tests = int(infile.readline())
    for i in xrange(1, num_tests + 1):
        start, end = infile.readline().split(' ')
        result = solve(int(start), int(end))
        print(u'Case #{}: {}'.format(i, result))


if __name__ == '__main__':
    sys.exit(main())

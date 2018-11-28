#!/usr/bin/env python
# vim: set fileencoding=utf-8
'''Module docstring
Template version: 1.2

Problem

The Dutch computer scientist Edsger Dijkstra made many important contributions
to the field, including the shortest path finding algorithm that bears his
name. This problem is not about that algorithm.

You were marked down one point on an algorithms exam for misspelling "Dijkstra"
-- between D and stra, you wrote some number of characters, each of which was
either i, j, or k. You are prepared to argue to get your point back using
quaternions, an actual number system (extended from complex numbers) with the
following multiplicative structure:



To multiply one quaternion by another, look at the row for the first quaternion
and the column for the second quaternion. For example, to multiply i by j, look
in the row for i and the column for j to find that the answer is k. To multiply
j by i, look in the row for j and the column for i to find that the answer is
-k.

As you can see from the above examples, the quaternions are not commutative --
that is, there are some a and b for which a * b != b * a. However they are
associative -- for any a, b, and c, it's true that a * (b * c) = (a * b) * c.

Negative signs before quaternions work as they normally do -- for any
quaternions a and b, it's true that -a * -b = a * b, and -a * b = a * -b = -(a
* b).

You want to argue that your misspelling was equivalent to the correct spelling
ijk by showing that you can split your string of is, js, and ks in two places,
forming three substrings, such that the leftmost substring reduces (under
quaternion multiplication) to i, the middle substring reduces to j, and the
right substring reduces to k. (For example, jij would be interpreted as j * i *
j; j * i is -k, and -k * j is i, so jij reduces to i.) If this is possible, you
will get your point back. Can you find a way to do it?

Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each consists of one line with two space-separated integers L and X,
followed by another line with L characters, all of which are i, j, or k. Note
that the string never contains negative signs, 1s, or any other characters. The
string that you are to evaluate is the given string of L characters repeated X
times. For instance, for L = 4, X = 3, and the given string kiij, your input
string would be kiijkiijkiij.

Output

For each test case, output one line containing "Case #x: y", where x is the
test case number (starting from 1) and y is either YES or NO, depending on
whether the string can be broken into three parts that reduce to i, j, and k,
in that order, as described above.

Limits

1 ≤ T ≤ 100.
1 ≤ L ≤ 10000.
Small dataset

1 ≤ X ≤ 10000.
1 ≤ L * X ≤ 10000.
Large dataset

1 ≤ X ≤ 1012.
1 ≤ L * X ≤ 1016.
Sample


Input

Output

5
2 1
ik
3 1
ijk
3 1
kji
2 6
ji
1 10000
i

Case #1: NO
Case #2: YES
Case #3: NO
Case #4: YES
Case #5: NO
In Case #1, the string is too short to be split into three substrings.

In Case #2, just split the string into i, j, and k.

In Case #3, the only way to split the string into three parts is k, j, i, and
this does not satisfy the conditions.

In Case #4, the string is jijijijijiji. It can be split into jij (which reduces
to i), iji (which reduces to j), and jijiji (which reduces to k).

In Case #5, no matter how you choose your substrings, none of them can ever
reduce to a j or a k.
'''

# for python2
from __future__ import division, print_function

VERSION = '%(prog)s 1.0'

import argparse
import sys
import os
import functools
import logging
#import heapq
#from operator import itemgetter
#from collections import defaultdict
#from collections import deque
#from array import array
#from bisect import bisect
#from math import sqrt
from itertools import groupby

#import cPickle

# for interactive call: do not add multiple times the handler
if 'LOG' not in locals():
    LOG = None
LOG_LEVEL = logging.ERROR
FORMATER_STRING = ('%(asctime)s - %(filename)s:%(lineno)d - '
                   '%(levelname)s - %(message)s')

def configure_log(level=LOG_LEVEL, log_file=None):
    'Configure logger'
    if LOG:
        LOG.setLevel(level)
        return LOG
    log = logging.getLogger('%s log' % os.path.basename(__file__))
    if log_file:
        handler = logging.FileHandler(filename=log_file)
    else:
        handler = logging.StreamHandler(sys.stderr)
    log_formatter = logging.Formatter(FORMATER_STRING)
    handler.setFormatter(log_formatter)
    log.addHandler(handler)
    log.setLevel(level)
    return log

LOG = configure_log()

# to be used as decorator so no capitalisation
# pylint: disable=invalid-name
class memoized(object):
    '''Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    '''
    # pylint: disable=too-few-public-methods
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        try:
            return self.cache[args]
        except KeyError:
            value = self.func(*args)
            self.cache[args] = value
            return value
        except TypeError:
            # uncachable -- for instance, passing a list as an argument.
            # Better to not cache than to blow up entirely.
            return self.func(*args)
    def __repr__(self):
        '''Return the function's docstring.'''
        return self.func.__doc__
    def __get__(self, obj, objtype):
        '''Support instance methods.'''
        return functools.partial(self.__call__, obj)
# pylint: enable=invalid-name

TARGET = 'ijk'

def inverse_sign(result):
    '''Return the result with opposite sign

    >>> inverse_sign('-i')
    'i'
    >>> inverse_sign('i')
    '-i'
    >>> inverse_sign('-1')
    '1'
    >>> inverse_sign('1')
    '-1'
    '''
    if result.startswith('-'):
        return result.lstrip('-')
    return '-' + result

def multiply(a, b):
    '''Return special multiplication

    >>> multiply('1', '1')
    '1'
    >>> multiply('i', '1')
    'i'
    >>> multiply('i', 'i')
    '-1'
    >>> multiply('i', 'j')
    'k'
    >>> multiply('j', 'i')
    '-k'
    >>> multiply('i', 'k')
    '-j'
    >>> multiply('k', 'i')
    'j'
    >>> multiply('j', 'k')
    'i'
    >>> multiply('k', 'j')
    '-i'
    >>> multiply('-k', '-j')
    '-i'
    >>> multiply('-k', 'j')
    'i'
    >>> multiply('k', '-j')
    'i'
    '''
    if not a:
        return b
    if not b:
        return a
    if a == '1':
        return b
    if b == '1':
        return a
    if a == b:
        return '-1'
    if a == 'i' and b == 'j':
        return 'k'
    if a == 'j' and b == 'i':
        return '-k'
    if a == 'i' and b == 'k':
        return '-j'
    if a == 'k' and b == 'i':
        return 'j'
    if a == 'j' and b == 'k':
        return 'i'
    if a == 'k' and b == 'j':
        return '-i'
    # negative cases
    if a.startswith('-'):
        return inverse_sign(multiply(a.lstrip('-'), b))
    if b.startswith('-'):
        return inverse_sign(multiply(a, b.lstrip('-')))
    assert False, 'a: %s, b: %s' % (a, b)

@memoized
def multiply_all(characters):
    '''Return the multiplication of all characters

    Dedicated function to benefit from memoization

    >>> multiply_all('11111')
    '1'
    >>> multiply_all('jjjjj')
    'j'
    >>> multiply_all('jij')
    'i'
    >>> multiply_all('iji')
    'j'
    >>> multiply_all('jijiji')
    'k'
    '''
    LOG.debug('called multiply_all with %s', characters)
    if not characters:
        return '1'
    if len(characters) == 1:
        return characters
    power_list = [(char, sum(1 for _ in group))
                  for char, group in groupby(characters)]
    pre_computed = ''.join((power(char, exponent)
                            for char, exponent in power_list))
    # split in half thanks to associativity
    middle = len(pre_computed) // 2
    return multiply(multiply_all(pre_computed[:middle]),
                    multiply_all(pre_computed[middle:]))

def power(character, exponent):
    '''Return the exponentiation of character

    >>> power('1', 33)
    '1'
    >>> power('j', 2)
    '-1'
    >>> power('j', 3)
    '-j'
    >>> power('j', 4)
    '1'
    >>> power('j', 5)
    'j'
    '''
    if character == '1':
        return '1'
    # all square evaluate to -1
    mod_4 = exponent % 4
    if mod_4 == 0:
        return '1'
    elif mod_4 == 1:
        return character
    elif mod_4 == 2:
        return '-1'
    elif mod_4 == 3:
        return inverse_sign(character)

def precompute_reverse(pattern):
    '''Return a list of position that produce a last part multiply matching
    last term of TARGET

    >>> precompute_reverse('jijijijijiji')
    [6]
    >>> precompute_reverse('jijijijijij')
    [9]
    >>> precompute_reverse('iiiiiiiiiii')
    []
    >>> precompute_reverse('iiik')
    [3]
    '''
    last_part_char = '1'
    pattern_length = len(pattern)
    matching_position = []
    for k in xrange(pattern_length - 1, 1, -1):
        last_part_char = multiply(pattern[k], last_part_char)
        if last_part_char == TARGET[2]:
            matching_position.append(k)
    return matching_position

def reduce_possible(pattern):
    '''Return True if the pattern can be reduced to TARGET
    '''
    pattern_length = len(pattern)
    if pattern_length < len(TARGET):
        return False
    # precompute reverse path
    matching_last_split = precompute_reverse(pattern)
    if not matching_last_split:
        return False
    # first split
    first_part_char = '1'
    #for i in xrange(pattern_length - 1):
    for i in xrange(max(matching_last_split) - 1):
        first_part_char = multiply(first_part_char, pattern[i])
        if first_part_char == TARGET[0]:
            # second split
            second_part_char = '1'
            for j in xrange(i + 1, pattern_length):
                second_part_char = multiply(second_part_char, pattern[j])
                if (second_part_char == TARGET[1]
                    and (j + 1) in matching_last_split):
                    return True
    return False

def do_job(in_file, out_file=sys.stdout):
    'Do the work'
    # sticking with names used in gcj
    # pylint: disable=invalid-name
    LOG.debug('Start working with files: %s and %s',
              in_file.name, out_file.name)
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in range(T):
        # for integer input
        L, X = [int(x) for x in in_file.readline().split()]
        # for other inputs
        pattern = in_file.readline().rstrip('\n')
        assert len(pattern) == L
        if L > 1:
            input_str = pattern * X
            LOG.debug(input_str)
            result = reduce_possible(input_str)
        else:
            result = False
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    'Formats and print result'
    print('Case #%d:' % (testcase + 1), end=' ', file=out_file)
    print('YES' if result else 'NO', file=out_file)
    #print('%.6g' % result, file=out_file)

def create_parser():
    'Return the argument parser'
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=VERSION)
    parser.add_argument('--debug', dest='debug', action='store_true',
                        help=argparse.SUPPRESS)
    verbosity = parser.add_mutually_exclusive_group()
    verbosity.add_argument('-q', '--quiet', '--silent', dest='quiet',
                           action='store_true', default=False,
                           help='run as quiet mode')
    verbosity.add_argument('-v', '--verbose', dest='verbose',
                           action='store_true', default=False,
                           help='run as verbose mode')
    parser.add_argument('-t', dest='template', action='store_true',
                        default=False,
                        help=('template name for construct'
                              'out file name as in_file.out (default False)'))
    parser.add_argument('-w', dest='out_file',
                        help=('output file or stdout if FILE is - '
                              '(default case) or TEMPLATE.out (default if '
                              'template is given)'))
    #type=argparse.FileType('w')
    parser.add_argument('in_file', help='input file (default stdin)',
                        default=sys.stdin, type=argparse.FileType('r'))
    return parser

def main(argv=None):
    'Program wrapper'
    if argv is None:
        argv = sys.argv[1:]
    parser = create_parser()
    args = parser.parse_args(argv)
    if args.verbose:
        LOG.setLevel(logging.INFO)
    if args.quiet:
        LOG.setLevel(logging.CRITICAL)
    if args.debug:
        LOG.setLevel(logging.DEBUG)
#    # unset verbose for easy option check
#    args.verbose = False
#    if not any(args.__dict__.values()):
#        parser.error('Must provide at least one option')
    if args.template and not args.out_file:
        args.out_file = ''.join((args.in_file.name, '.out'))
    if not args.out_file or args.out_file == '-':
        out_file = sys.stdout
    else:
        try:
            out_file = open(args.out_file, 'w')
        except IOError:
            parser.error('Problem opening file: %s' % args.out_file)
    #sys.setrecursionlimit(2**30-1)
    #MULTIPLY_CACHE.update(cPickle.load(open(MULTIPLY_CACHE_FILE)))
    do_job(args.in_file, out_file)
    #cPickle.dump(MULTIPLY_CACHE, open(MULTIPLY_CACHE_FILE, 'wb'))
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())


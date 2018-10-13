#!/usr/bin/env pypy
# vim: set fileencoding=utf-8
'''Module docstring
Template version: 1.2


Problem

Your publishing house has decided to use monkeys randomly typing at keyboards
to write great works of literature. You are the supervisor for one monkey with
a keyboard containing K keys, each of which is labeled with an uppercase
English letter. (There may be multiple keys displaying the same letter.) The
monkey will start with an empty string and repeat the following S times: choose
a key from its keyboard uniformly at random and press it, adding a copy of that
key's letter to the right end of the string. The final resulting string will
have length S.

You have a target word of length L that you are hoping the monkey will type.
(The target word will not necessarily be a real English word.) This target word
may even appear multiple times in what the monkey types. (Overlapping instances
count too -- for example, if "ABA" is the target word and the monkey types
"ABABA", that contains two instances of the target.)

You plan to pay the monkey one banana for each instance of the target word that
it types. When you go to inspect the monkey's work, you will bring along the
minimum number of bananas that you need to ensure that you will always have
enough bananas to pay the monkey, no matter what it has typed. Then, you will
pay the monkey one banana for each instance of the target word that it actually
typed. You will keep the remaining bananas that you brought with you.

What is the expected number of bananas that you will get to keep?
Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each consists of three lines. The first contains three space-separated
positive integers: K, L, and S. The second contains a string of K uppercase
English letters representing the monkey's keyboard. The third contains a string
of L uppercase English letters representing the target word.

Output

For each test case, output one line containing "Case #x: y", where y is the
expected number of bananas you will get to keep after paying the monkey.

y will be considered correct if it is within an absolute or relative error of
10-6 of the correct answer. See the FAQ for an explanation of what that means,
and what formats of real numbers we accept.
Limits

1 ≤ T ≤ 100.
Small dataset

1 ≤ K ≤ 7.
1 ≤ L ≤ S ≤ 7.
Large dataset

1 ≤ K ≤ 100.
1 ≤ L ≤ S ≤ 100.
Sample


Input

Output

5
7 6 6
BANANAS
MONKEY
2 3 4
AA
AAA
2 1 2
AB
B
6 2 2
GOOGLE
GO
26 11 100
ABCDEFGHIJKLMNOPQRSTUVWXYZ
ROSENCRANTZ

Case #1: 0.0
Case #2: 0.0
Case #3: 1.0
Case #4: 0.8888889
Case #5: 9.0

Note that Case #5 is not within the limits for the Small dataset.

In Case #1, the monkey has no chance of typing the target word "MONKEY" even
once (because his keyboard lacks most of the letters in "MONKEY"), so you do
not bring any bananas along when you visit, and of course you do not pay any.
Poor monkey!

In Case #2, the monkey is guaranteed to type "AAAA", which has two overlapping
instances of the target word "AAA". You will bring two bananas and then pay
both.

In Case #3, the monkey will produce the following outputs with equal
probability (1/4 each): "AA", "AB", "BA", "BB". These have 0, 1, 1, and 2
instances of the target word, respectively. You must bring 2 bananas to be
ready for the "BB" case, but you will on average pay (0 + 1 + 1 + 2) / 4 = 1.

In Case #4, the monkey has a 1/3 chance of typing a "G" first and a 1/3 chance
of typing an "O" second, for a 1/9 chance of typing "GO". You will bring one
banana and give it up 1/9 of the time.

In Case #5, the monkey could in theory type "ROSENCRANTZ" up to nine times, but
the chances of this happening even once are so small that they are negligible
compared to the acceptable margin of error for answers.
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

import itertools

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

class CommentedFile(object):
    'Implements comments skip for file'
    # pylint: disable=too-few-public-methods
    def __init__(self, in_file, commentstring='#'):
        self.in_file = in_file
        self.commentstring = commentstring
    def next(self):
        'The next line but skips comments'
        line = self.in_file.next()
        while line.startswith(self.commentstring):
            line = self.in_file.next()
        return line
    def __iter__(self):
        return self

def compute_expected(S, target, keyboard):
    '''Return the expected prob of giving bananas
    '''
    for key in set(target):
        if key not in keyboard:
            return 0
    successes = []
    total_nb = 0
    for output in itertools.product(keyboard, repeat=S):
        total_nb += 1
        output = ''.join(output)
        index = output.find(target)
        success = 0
        while index >= 0:
            success += 1
            index = output.find(target, index + 1)
        successes.append(success)
    bananas_brought = max(successes)
    return bananas_brought - (sum(successes) / total_nb)

def do_job(in_file, out_file=sys.stdout):
    'Do the work'
    # sticking with names used in gcj
    # pylint: disable=invalid-name
    LOG.debug('Start working with files: %s and %s',
              in_file.name, out_file.name)
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in range(T):
        #N = int(in_file.readline())
        # for integer input
        K, L, S = [int(x) for x in in_file.readline().split()]
        # for other inputs
        keyboard = in_file.readline().rstrip('\n')
        assert len(keyboard) == K
        target = in_file.readline().rstrip('\n')
        assert len(target) == L
        result = compute_expected(S, target, keyboard)
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    'Formats and print result'
    print('Case #%d:' % (testcase + 1), end=' ', file=out_file)
    #print(result, file=out_file)
    print('%.6f' % result, file=out_file)
    out_file.flush()

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
    sys.setrecursionlimit(2**30-1)
    do_job(args.in_file, out_file)
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())


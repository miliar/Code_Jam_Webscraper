#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Problem

Goro has 4 arms. Goro is very strong. You don't mess with Goro. Goro needs to
sort an array of N different integers. Algorithms are not Goro's strength;
strength is Goro's strength. Goro's plan is to use the fingers on two of his
hands to hold down several elements of the array and hit the table with his
third and fourth fists as hard as possible. This will make the unsecured
elements of the array fly up into the air, get shuffled randomly, and fall back
down into the empty array locations.

Goro wants to sort the array as quickly as possible. How many hits will it take
Goro to sort the given array, on average, if he acts intelligently when
choosing which elements of the array to hold down before each hit of the table?

More precisely, before each hit, Goro may choose any subset of the elements of
the array to freeze in place. He may choose differently depending on the
outcomes of previous hits. Each hit permutes the unfrozen elements uniformly at
random. Each permutation is equally likely.  Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each one will consist of two lines. The first line will give the number
N. The second line will list the N elements of the array in their initial
order.  Output

For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1) and y is the expected number of hit-the-table
operations when following the best hold-down strategy. Answers with an absolute
or relative error of at most 10-6 will be considered correct.  Limits

1 ≤ T ≤ 100; The second line of each test case will contain a permutation of
  the N smallest positive integers.  Goro has more than N fingers on each hand.
  Small dataset

1 ≤ N ≤ 10;

Large dataset

1 ≤ N ≤ 1000;

Sample

Input

3
2
2 1
3
1 3 2
4
2 1 4 3

Output

Case #1: 2.000000
Case #2: 2.000000
Case #3: 4.000000

Explanation In test case #3, one possible strategy is to hold down the two
leftmost elements first. Elements 3 and 4 will be free to move. After a table
hit, they will land in the correct order [3, 4] with probability 1/2 and in the
wrong order [4, 3] with probability 1/2. Therefore, on average it will take 2
hits to arrange them in the correct order. After that, Goro can hold down
elements 3 and 4 and hit the table until 1 and 2 land in the correct order,
which will take another 2 hits, on average. The total is then 2 + 2 = 4 hits.
"""

from __future__ import division, print_function
from optparse import OptionParser
import sys
import functools
import logging

def configure_log(log_file=None):
    "Configure the log output"
    log_formatter = logging.Formatter("%(asctime)s - %(filename)s:%(lineno)d - "
                                      "%(levelname)s - %(message)s")
    if log_file:
        handler = logging.FileHandler(filename=log_file)
    else:
        handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(log_formatter)
    LOG.addHandler(handler)

LOG = None
# for interactive call: do not add multiple times the handler
if not LOG:
    LOG = logging.getLogger('template')
    configure_log()

class memoized(object):
    """Decorator that caches a function's return value each time it is called.
    If called later with the same arguments, the cached value is returned, and
    not re-evaluated.
    """
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
        """Return the function's docstring."""
        return self.func.__doc__
    def __get__(self, obj, objtype):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

def get_split(values):
    """Return 2 lists with the best split:
    try to find the pivot of elements
    >>> get_split([2, 1, 4, 3]) # ([2, 1], [4, 3])
    2
    >>> get_split([2, 1, 4, 5]) # ([2, 1], [4, 5])
    2
    >>> get_split([2, 1, 4, 6, 5]) # ([2, 1], [4, 6, 5])
    2
    >>> get_split([2, 3, 1, 6, 5]) # ([2, 3, 1], [6, 5])
    3
    >>> get_split([6, 5, 4, 3, 2, 1]) # ([], [6, 5, 4, 3, 2, 1])
    0
    """
    sorted_values = sorted(values)
    good_split = 0
    for i in xrange(1, len(values)):
        if sorted(values[:i]) == sorted_values[:i]:
            good_split = i
            break
    return good_split

def sort_hits(values):
    """Returns the number of hits goro has to do to sort the list
    First try to sort most elements together: mins at left maxs at right
    """
    hits = 0
    for a, b in zip(values, sorted(values)):
        if a == b:
            LOG.debug('remove already sorted element: %d' % a)
            values.remove(a)
    len_values = len(values)
    # why not...
    return len_values
    if len_values <= 1:
        LOG.debug('no more hit: UNEXPECTED')
        pass
    elif len_values == 2:
        hits += 2
    else:
        good_split = get_split(values)
        if good_split != 0:
            LOG.debug('values splitted as: %s, %s'
                      % (values[:good_split], values[good_split:]))
            hits = (sort_hits(values[:good_split])
                    + sort_hits(values[good_split:]))
        else:
            LOG.debug('no good split: place min at its place in %s' % values)
            min_index = values.index(min(values))
            values[min_index], values[0] = values[0], values[min_index]
            hits += 2 + sort_hits(values)
    return hits

def do_job(in_file, out_file):
    "Do the work"
    LOG.debug("Start working with files: %s and %s"
              % (in_file.name, out_file.name))
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in xrange(T):
        # for integer input
        N = int(in_file.readline())
        values = map(int, in_file.readline().split())
        assert len(values) == N
        result = sort_hits(values)
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    "Formats and print result"
    print("Case #%d:" % (testcase + 1), end=' ', file=out_file)
    print('%.6f' % result, file=out_file)

def main(argv=None):
    "Program wrapper."
    if argv is None:
        argv = sys.argv[1:]
    usage = "%prog [-v] [-w out_file] [-t] in_file"
    parser = OptionParser(usage=usage)
    parser.add_option("-t", dest="template", action="store_true", default=False,
                      help=("template name for construct"
                            "out file name as in_file.out (default False)"))
    parser.add_option("-w", dest="out_file",
            help=("output file or stdout if FILE is - (default case)"
                  "or TEMPLATE.out (default if template is given)"))
    parser.add_option("-v", "--verbose", dest="verbose",
            action="store_true", default=False,
            help = "run as verbose mode")
    (options, args) = parser.parse_args(argv)
    if not args:
        parser.error('no input file given')
    if options.verbose:
        LOG.setLevel(logging.DEBUG)
    if args[0] == '-':
        in_file = sys.stdin
    else:
        try:
            in_file = open(args[0], 'r')
        except IOError:
            parser.error("File, %s, does not exist." % args[0])
    if options.template and not options.out_file:
        options.out_file = ''.join((args[0], '.out'))
    if not options.out_file or options.out_file == '-':
        out_file = sys.stdout
    else:
        try:
            out_file = open(options.out_file, 'w')
        except IOError:
            parser.error("Problem opening file: %s" % options.out_file)
    sys.setrecursionlimit(2**31-1)
    do_job(in_file, out_file)
    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    sys.exit(main())

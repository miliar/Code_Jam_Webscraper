#!/usr/bin/env python
# vim: set fileencoding=utf-8 :

"""Introduction

Magicka™ is an action-adventure game developed by Arrowhead Game Studios. In
Magicka you play a wizard, invoking and combining elements to create Magicks.
This problem has a similar idea, but it does not assume that you have played
Magicka.

Note: "invoke" means "call on." For this problem, it is a technical term and
you don't need to know its normal English meaning.  Problem

As a wizard, you can invoke eight elements, which are the "base" elements. Each
base element is a single character from {Q, W, E, R, A, S, D, F}. When you
invoke an element, it gets appended to your element list. For example: if you
invoke W and then invoke A, (we'll call that "invoking WA" for short) then your
element list will be [W, A].

We will specify pairs of base elements that combine to form non-base elements
(the other 18 capital letters). For example, Q and F might combine to form T.
If the two elements from a pair appear at the end of the element list, then
both elements of the pair will be immediately removed, and they will be
replaced by the element they form. In the example above, if the element list
looks like [A, Q, F] or [A, F, Q] at any point, it will become [A, T].

We will specify pairs of base elements that are opposed to each other. After
you invoke an element, if it isn't immediately combined to form another
element, and it is opposed to something in your element list, then your element
list will be cleared.

For example, suppose Q and F combine to make T. R and F are opposed to each
other. Then invoking the following things (in order, from left to right) will
have the following results:

    * QF → [T] (Q and F combine to form T) QEF → [Q, E, F] (Q and F can't
    * combine because they were never at the end of the element list together)
    * RFE → [E] (F and R are opposed, so the list is cleared; then E is
    * invoked) REF → [] (F and R are opposed, so the list is cleared) RQF → [R,
    * T] (QF combine to make T, so the list is not cleared) RFQ → [Q] (F and R
    * are opposed, so the list is cleared)

Given a list of elements to invoke, what will be in the element list when
you're done?  Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each test case consists of a single line, containing the following
space-separated elements in order:

First an integer C, followed by C strings, each containing three characters:
two base elements followed by a non-base element. This indicates that the two
base elements combine to form the non-base element. Next will come an integer
D, followed by D strings, each containing two characters: two base elements
that are opposed to each other. Finally there will be an integer N, followed by
a single string containing N characters: the series of base elements you are to
invoke. You will invoke them in the order they appear in the string (leftmost
character first, and so on).  Output

For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1) and y is a list in the format "[e0, e1, ...]"
where ei is the ith element of the final element list. Please see the sample
output for examples.  Limits

1 ≤ T ≤ 100.  Each pair of base elements may only appear together in one
  combination, though they may appear in a combination and also be opposed to
  each other.  No base element may be opposed to itself.  Unlike in the
  computer game Magicka, there is no limit to the length of the element list.

  Small dataset

0 ≤ C ≤ 1.
0 ≤ D ≤ 1.
1 ≤ N ≤ 10.

Large dataset

0 ≤ C ≤ 36.
0 ≤ D ≤ 28.
1 ≤ N ≤ 100.

Sample

Input

5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW

Output

Case #1: [E, A]
Case #2: [R, I, R]
Case #3: [F, D, T]
Case #4: [Z, E, R, A]
Case #5: []
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

def prune_elements(current_elements, opposite, combine):
    "Transforms elements in list"
    while len(current_elements) >= 2:
        try_again = False
        # first combine
        combine_key = ''.join(sorted(current_elements[-2:]))
        if combine_key in combine:
            LOG.debug('combining elements: %s' % current_elements[-2:])
            current_elements = ''.join((current_elements[:-2],
                                        combine[combine_key]))
            try_again = True
        # then oppose
        if len(current_elements) >= 2:
            for opposite_elements in opposite:
                if (opposite_elements[0] in current_elements
                    and opposite_elements[1] in current_elements):
                    # shortcut
                    return ''
        # nothing else to combine
        if not try_again:
            break
    return current_elements

def process(elements, opposite, combine):
    "Process one game"
    current_elements = ''
    for elem in elements:
        current_elements = ''.join((current_elements, elem))
        current_elements = prune_elements(current_elements, opposite, combine)
    return current_elements

def do_job(in_file, out_file):
    "Do the work"
    LOG.debug("Start working with files: %s and %s"
              % (in_file.name, out_file.name))
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in xrange(T):
        # for integer input
#        values = map(int, in_file.readline().split())
        # for other inputs
        values = in_file.readline().rstrip('\n').split()
        C = int(values.pop(0))
        combine = {}
        for _ in xrange(C):
            combine_elements = values.pop(0)
            assert len(combine_elements) == 3
            combine[''.join(sorted(combine_elements[:2]))] = combine_elements[2]
        LOG.info('combine elements: %s' % combine)
        D = int(values.pop(0))
        opposite = {}
        for _ in xrange(D):
            opposite_elements = values.pop(0)
            assert len(opposite_elements) == 2
            opposite[''.join(sorted(opposite_elements))] = True
        LOG.info('opposite elements: %s' % opposite)
        N = int(values.pop(0))
        elements = values.pop(0)
        assert len(elements) == N
        # all input processed
        assert (not values)
        result = process(elements, opposite, combine)
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    "Formats and print result"
    print("Case #%d:" % (testcase + 1), end=' ', file=out_file)
    print(str(list(result)).translate(None, "'"), file=out_file)

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
    sys.exit(main())

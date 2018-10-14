#!/usr/bin/env python
"""Problem

Blue and Orange are friendly robots. An evil computer mastermind has locked
them up in separate hallways to test them, and then possibly give them cake.

Each hallway contains 100 buttons labeled with the positive integers {1, 2,
..., 100}. Button k is always k meters from the start of the hallway, and the
robots both begin at button 1. Over the period of one second, a robot can walk
one meter in either direction, or it can press the button at its position once,
or it can stay at its position and not press the button. To complete the test,
the robots need to push a certain sequence of buttons in a certain order. Both
robots know the full sequence in advance. How fast can they complete it?

For example, let's consider the following button sequence:

   O 2, B 1, B 2, O 4

Here, O 2 means button 2 in Orange's hallway, B 1 means button 1 in Blue's
hallway, and so on. The robots can push this sequence of buttons in 6 seconds
using the strategy shown below:

Time | Orange           | Blue
-----+------------------+-----------------
  1  | Move to button 2 | Stay at button 1
  2  | Push button 2    | Stay at button 1
  3  | Move to button 3 | Push button 1
  4  | Move to button 4 | Move to button 2
  5  | Stay at button 4 | Push button 2
  6  | Push button 4    | Stay at button 2

Note that Blue has to wait until Orange has completely finished pushing O 2
before it can start pushing B 1.  Input

The first line of the input gives the number of test cases, T. T test cases
follow.

Each test case consists of a single line beginning with a positive integer N,
representing the number of buttons that need to be pressed. This is followed by
N terms of the form "Ri Pi" where Ri is a robot color (always 'O' or 'B'), and
Pi is a button position.  Output

For each test case, output one line containing "Case #x: y", where x is the
case number (starting from 1) and y is the minimum number of seconds required
for the robots to push the given buttons, in order.  Limits

1 < Pi < 100 for all i.
Small dataset

1 < T < 20.
1 < N < 10.

Large dataset

1 < T < 100.
1 < N < 100.

Sample

Input

3
4 O 2 B 1 B 2 O 4
3 O 5 O 8 B 100
2 B 2 B 1

Output

Case #1: 6
Case #2: 100
Case #3: 4

"""

from __future__ import division, print_function
from optparse import OptionParser
import sys
import functools
import logging
from collections import defaultdict

def configure_log(log_file=None):
    "Configure the log output"
    log_formatter = logging.Formatter("%(asctime)s - %(funcName)s:%(lineno)d - "
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

def process(moves, N):
    "Process the input moves and return the total time"
    time = 0
    pos = {'O': 1, 'B': 1}
    index = {'O': 0, 'B': 0}
    length = {'O': len(moves['O']), 'B': len(moves['B'])}
    button_pressed = 0
    while button_pressed < N:
        press_only_once = True
        to_remove = []
        for robot in moves:
            if index[robot] < length[robot]:
                position, order = moves[robot][index[robot]]
                if pos[robot] == position:
                    LOG.debug('robot %s in position to press with order %d'
                              % (robot, pos[robot]))
                    if order == button_pressed and press_only_once:
                        LOG.debug('robot %s press button' % robot)
                        button_pressed += 1
                        press_only_once = False
                        index[robot] += 1
                elif pos[robot] > position:
                    pos[robot] -= 1
                    LOG.debug('robot %s move back to pos: %d'
                              % (robot, pos[robot]))
                elif pos[robot] < position:
                    pos[robot] += 1
                    LOG.debug('robot %s move forward to pos: %d'
                              % (robot, pos[robot]))
                else:
                    LOG.error('incorrect position')
            else:
                LOG.info('no more move for robot %s' % robot)
                to_remove.append(robot)
        for robot in to_remove:
            moves.pop(robot)
        time += 1
    return time

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
        N = int(values.pop(0))
        moves = defaultdict(list)
        for order in xrange(N):
            robot = values.pop(0)
            position = int(values.pop(0))
            moves[robot].append((position, order))
        LOG.debug(moves)
        result = process(moves, N)
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    "Formats and print result"
    print("Case #%d:" % (testcase + 1), end=' ', file=out_file)
    print(result, file=out_file)

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

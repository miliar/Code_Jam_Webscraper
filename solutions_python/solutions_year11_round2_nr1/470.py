#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Module docstring
Problem

In the United States, 350 schools compete every year for an invitation to the
NCAA College Basketball Tournament. With so many schools, how do you decide who
should be invited? Most teams never play each other, and some teams have a much
more difficult schedule than others.

Here is an example schedule for 4 teams named A, B, C, D:

   |ABCD -+---- A|.11.  B|0.00 C|01.1 D|.10.

Each 1 in a team's row represents a win, and each 0 represents a loss. So team
C has wins against B and D, and a loss against A. Team A has wins against B and
C, but has not played D.

The NCAA tournament committee uses a formula called the RPI (Ratings Percentage
Index) to help rank teams. Traditionally, it has been defined as follows:

  RPI = 0.25 * WP + 0.50 * OWP + 0.25 * OOWP

WP, OWP, and OOWP are defined for each team as follows:

    WP (Winning Percentage) is the fraction of your games that you have won.
    In the example schedule, team A has WP = 1, team B has WP = 0, team C has
    WP = 2/3, and team D has WP = 0.5.  OWP (Opponents' Winning Percentage) is
    the average WP of all your opponents, after first throwing out the games
    they played against you.  For example, if you throw out games played
    against team D, then team B has WP = 0 and team C has WP = 0.5. Therefore
    team D has OWP = 0.5 * (0 + 0.5) = 0.25. Similarly, team A has OWP = 0.5,
    team B has OWP = 0.5, and team C has OWP = 2/3.  OOWP (Opponents'
    Opponents' Winning Percentage) is the average OWP of all your opponents.
    OWP is exactly the number computed in the previous step.  For example, team
    A has OOWP = 0.5 * (0.5 + 2/3) = 7/12.

Putting it all together, we see team A has RPI = (0.25 * 1) + (0.5 * 0.5) +
(0.25 * 7 / 12) = 0.6458333...

There are some pretty interesting questions you can ask about the RPI. Is it a
reasonable measure of team's ability? Is it more important for teams to win
games, or to schedule strong opponents? These are all good questions, but for
this problem, your task is more straightforward: given a schedule of games, can
you calculate every team's RPI?

Input

The first line of the input gives the number of test cases, T. T test cases
follow. Each test case begins with a single line containing the number of teams
N.

The next N lines each contain exactly N characters (either '0', '1', or '.')
representing a schedule in the same format as the example schedule above. A '1'
in row i, column j indicates team i beat team j, a '0' in row i, column j
indicates team i lost to team j, and a '.' in row i, column j indicates team i
never played against team j.  Output

For each test case, output N + 1 lines. The first line should be "Case #x:"
where x is the case number (starting from 1). The next N lines should contain
the RPI of each team, one per line, in the same order as the schedule.

Answers with a relative or absolute error of at most 10-6 will be considered
correct.  Limits

1 ≤ T ≤ 20.  If the schedule contains a '1' in row i, column j, then it
  contains a '0' in row j, column i.  If the schedule contains a '0' in row i,
  column j, then it contains a '1' in row j, column i.  If the schedule
  contains a '.' in row i, column j, then it contains a '.' in row j, column i.
  Every team plays at least two other teams.  No two teams play each other
  twice.  No team plays itself.  Small dataset

3 ≤ N ≤ 10.  Large dataset

3 ≤ N ≤ 100.  Sample

Input

2
3
.10
0.1
10.
4
.11.
0.00
01.1
.10.

Output
Case #1:
0.5
0.5
0.5
Case #2:
0.645833333333
0.368055555556
0.604166666667
0.395833333333

"""

from __future__ import division, print_function
from optparse import OptionParser
import sys
import functools
import logging
#from collections import defaultdict
from numpy import average

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

def convert_values(values):
    """convert the input string to ints or None
    >>> convert_values('01.')
    [0, 1, None]
    """
    scores = []
    for v in values:
        if v == '.':
            scores.append(None)
        else:
            scores.append(int(v))
    return scores

def compute_nb_wl(scores):
    """Compute the nb win and loss for the score list"""
    filtered_scores = filter(lambda x: x != None, scores)
    return (sum(filtered_scores), len(filtered_scores))

def opposite(s):
    "Returns the boolean opposite of s"
    if s == 0:
        return 1
    elif s== 1:
        return 0
    else:
        LOG.error('unexpected input: %s' % s)
def compute_rpi(scores):
    """Computes the RPI of the team"""
    #nb_wl = map(compute_nb_wl, scores)
    wps = []
    table_owps = []
    for score in scores:
        win, nb = compute_nb_wl(score)
        owp = []
        wps.append(win / nb)
        for s in score:
            if s != None:
                owp.append(max(win - s, 0) / (nb - 1))
            else:
                owp.append(None)
        table_owps.append(owp)
    # construct real owp
    owps = map(average,
               [filter(lambda x: x!= None, y) for y in zip(*table_owps)])
    LOG.debug([x for x in enumerate(owps)])
    rpis = []
    for i, score in enumerate(scores):
        oowp = average([owps[j] for j, v in enumerate(score) if v != None])
        rpis.append(0.25 * wps[i] + 0.5 * owps[i] + 0.25 * oowp)
    return rpis

def do_job(in_file, out_file=sys.stdout):
    "Do the work"
    LOG.debug("Start working with files: %s and %s"
              % (in_file.name, out_file.name))
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in xrange(T):
        N = int(in_file.readline())
        # for integer input
        #values = map(int, in_file.readline().split())
        # for other inputs
        scores = []
        for i in xrange(N):
            values = in_file.readline().rstrip('\n')
            assert len(values) == N
            scores.append(convert_values(values))
        result = compute_rpi(scores)
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    "Formats and print result"
    print("Case #%d:" % (testcase + 1), file=out_file)
    for score in result:
        print('%.12g' % score, file=out_file)

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

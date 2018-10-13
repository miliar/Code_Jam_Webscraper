#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
"""Module docstring
Problem

You are selling beautiful geometric pictures. Each one consists of 1x1 square
tiles arranged into a non-overlapping grid. For example:

    .##..  .#### .#### .##..

Blue tiles are represented by '#' characters, and white tiles are represented
by '.' characters. You do not use other colors.

Not everybody likes blue though, and some customers want you to replace all the
blue tiles in your picture with red tiles. Unfortunately, red tiles only come
in the larger 2x2 size, which makes this tricky.

You can cover any 2x2 square of blue tiles with a single red tile, and then
repeat until finished. A red tile cannot overlap another red tile, it cannot
cover white tiles, and it cannot go outside the picture. For example, you could
add red tiles to the previous picture as follows:

    ./\..  .\//\ ./\\/ .\/..

Each red tile is represented here by a pair of '/' characters in the top-left
and bottom-right corners, and a pair of '\' characters in the other two
corners.

Given a blue and white picture, can you transform it into a red and white
picture in this way?  Input

The first line of the input gives the number of test cases, T. T test cases
follow.

Each test case begins with a line containing R and C, the number of rows and
columns in a picture. The next R lines each contain exactly C characters,
describing the picture. As above, '#' characters represent blue tiles, and '.'
characters represent white tiles.  Output

For each test case, first output one line containing "Case #x:" where x is the
case number (starting from 1).

If it is possible to cover the blue tiles with non-overlapping red tiles,
output R lines each containing C characters, describing the resulting red and
white picture. As above, red tiles should be represented by '/' and '\'
characters, while white tiles are represented by '.' characters. If multiple
solutions are possible, you may output any of them.

If the task is impossible, output a single line containing the text
"Impossible" instead.  Limits Small dataset

1 ≤ T ≤ 20.
1 ≤ R ≤ 6.
1 ≤ C ≤ 6.  Large dataset

1 ≤ T ≤ 50.
1 ≤ R ≤ 50.
1 ≤ C ≤ 50.

Sample

Input

3
2 3
###
###
1 1
.
4 5
.##..
.####
.####
.##..

Output

Case #1:
Impossible
Case #2:
.
Case #3:
./\..
.\//\
./\\/
.\/..

"""

from __future__ import division, print_function
from optparse import OptionParser
import sys
import functools
import logging
from copy import deepcopy

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
    >>> convert_values('.##.')
    [False, True, True, False]
    """
    colors = []
    for v in values:
        if v == '.':
            colors.append(False)
        else:
            colors.append(True)
    return colors

def replace_blue(tiles, R, C):
    "Replace blue tiles with red ones"
    new_tiles = []
    for _ in xrange(R):
        new_tiles.append([])
        for _ in xrange(C):
            new_tiles[-1].append(None)
    i = 0
    for i, row in enumerate(tiles):
        for j, cur_pos in enumerate(row):
            if new_tiles[i][j]:
                LOG.debug((i, j))
                #print('\n'.join(map(str, new_tiles)))
                continue
            if not cur_pos:
                # white: just put '.'
                new_tiles[i][j] = '.'
            else:
                # try to replace with red
                if not all([tiles[i][j], tiles[i][j+1],
                            tiles[i+1][j], tiles[i+1][j+1]]):
                    return False
                new_tiles[i][j] = '/'
                new_tiles[i][j+1] = '\\'
                new_tiles[i+1][j] = '\\'
                new_tiles[i+1][j+1] = '/'
    output = '\n'.join([''.join(row) for row in new_tiles])
    return output

def do_job(in_file, out_file=sys.stdout):
    "Do the work"
    LOG.debug("Start working with files: %s and %s"
              % (in_file.name, out_file.name))
    # first line is number of test cases
    T = int(in_file.readline())
    for testcase in xrange(T):
        R, C = map(int, in_file.readline().split())
        tiles = []
        for _ in xrange(R):
            values = in_file.readline().rstrip()
            assert len(values) == C
            tiles.append(convert_values(values))
        assert len(tiles) == R
        result = None
        try:
            result = replace_blue(tiles, R, C)
        except IndexError:
            pass
        except Exception, e:
            LOG.exception(e)
        if not result:
            result = 'Impossible'
        print_output(out_file, testcase, result)

def print_output(out_file, testcase, result):
    "Formats and print result"
    print("Case #%d:" % (testcase + 1),  file=out_file)
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
    import doctest
    doctest.testmod()
    sys.exit(main())

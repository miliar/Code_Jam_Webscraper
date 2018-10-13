""" Saving the Universe

:Abstract: Solution to Google Code Jam 2008 practice problem.
:Authors:  iki
:Contact:  jan.killian at (g)mail.com

.. contents::

Problem statement
=================

The urban legend goes that if you go to the Google homepage and search for
"Google", the universe will implode. We have a secret to share... It is
true! Please don't try it, or tell anyone. All right, maybe not. We are
just kidding.

The same is not true for a universe far far away. In that universe, if you
search on any search engine for that search engine's name, the universe
does implode!

To combat this, people came up with an interesting solution. All queries
are pooled together. They are passed to a central system that decides which
query goes to which search engine. The central system sends a series of
queries to one search engine, and can switch to another at any time.
Queries must be processed in the order they're received. The central system
must never send a query to a search engine whose name matches the query. In
order to reduce costs, the number of switches should be minimized.

Your task is to tell us how many times the central system will have to
switch between search engines, assuming that we program it optimally.

Input
-----

The first line of the input file contains the number of cases, N. N test
cases follow.

Each case starts with the number S -- the number of search engines. The
next S lines each contain the name of a search engine. Each search engine
name is no more than one hundred characters long and contains only
uppercase letters, lowercase letters, spaces, and numbers. There will not
be two search engines with the same name.

The following line contains a number Q -- the number of incoming queries.
The next Q lines will each contain a query. Each query will be the name of
a search engine in the case.

Output
------

For each input case, you should output:

Case #X: Y

where X is the number of the test case and Y is the number of search engine
switches. Do not count the initial choice of a search engine as a switch.

Limits
------

0 < N <= 20

Small dataset

2 <= S <= 10

0 <= Q <= 100

Large dataset

2 <= S <= 100

0 <= Q <= 1000


Doctest
=======

Problem sample:

>>> from cStringIO import StringIO
>>> test(run,
...   testlabel='sample (via parser)',
...   *parse(StringIO('''2
... 5
... Yeehaw
... NSM
... Dont Ask
... B9
... Googol
... 10
... Yeehaw
... Yeehaw
... Googol
... B9
... Googol
... NSM
... B9
... NSM
... Dont Ask
... Googol
... 5
... Yeehaw
... NSM
... Dont Ask
... B9
... Googol
... 7
... Googol
... Dont Ask
... NSM
... NSM
... Yeehaw
... Yeehaw
... Googol
... ''')))
Case #1: 1
Case #2: 0

    * In the first case, one possible solution is to start by using Dont Ask, and switch to NSM after query number 8.
      For the second case, you can use B9, and not need to make any switches.


>>> test(run, [[3, iter([0, 1, 0, 1, 0, 1])]],
...   testlabel='3.1')
Case #1: 0

>>> test(run, [[3, iter([0, 1, 0, 1, 0, 1, 2])]],
...   testlabel='3.2')
Case #1: 1

>>> test(run, [[3, iter([0, 1, 0, 1, 0, 1, 2, 1])]],
...   testlabel='3.3')
Case #1: 1

>>> test(run, [[3, iter([0, 1, 0, 1, 0, 1, 2, 0])]],
...   testlabel='3.4')
Case #1: 1

>>> test(run, [[3, iter([0, 1, 0, 1, 0, 1, 2, 0, 1])]],
...   testlabel='3.5')
Case #1: 2

>>> test(run, [[3, iter([0, 1, 0, 1, 2, 0, 1, 2])]],
...   testlabel='3.6')
Case #1: 2

>>> test(run, [[3, iter([0, 1, 0, 1, 2, 0, 2, 0])]],
...   testlabel='3.7')
Case #1: 1

>>> test(run, [[3, iter([0, 1, 0, 1, 2, 0, 2, 0, 1])]],
...   testlabel='3.8')
Case #1: 2

>>> test(run, [[3, iter([0, 1, 0, 1, 2, 0, 2, 0, 1, 2])]],
...   testlabel='3.9')
Case #1: 2



"""

__docformat__ = 'restructuredtext en'

from heapq import heapify, heappop, heappush
from collections import deque
from itertools import izip, count
from string import maketrans

log = None
debug = None

### solution

def min_switches(N, queries):
    state = [0] * N  # for each engine: track lowest possible switches needed to be current engine
    try:
        last = queries.next()
    except StopIteration:
        return 0

    if debug: debug('%02d: %s' % (last, ','.join(map(str, state))))
    for q in queries:
        if q != last:
            state[last] = map_except(min, state, last) + 1
            last = q
        if debug: debug('%02d: %s' % (last, ','.join(map(str, state))))
    state[last] += 1 # to not give false lowest result
    return min(state)

def map_except(func, lst, exc):
    """ if the func does not accept empty list, it will fail for len(lst) < 2 obviously
    """
    if exc <= 0:
        return func(lst[1:])
    elif exc >= len(lst) - 1:
        return func(lst[:-1])
    else:
        return func(func(lst[:exc]), func(lst[exc+1:]))

def results(it):
    return '\n'.join('Case #%d: %d' % (c, min_switches(*i)) for i,c in izip(it, count(1)))

### parser

def parser(fi):
    return [parser_cases(fi)]

def parser_cases(fi, require=1):
    nl = fi.next
    N = n = int(nl().strip())
    if n < require:
        raise ValueError, '%d < %d' % (n, require)

    while n:
        n -= 1
        engines = list(parser_engines(nl, require=2))
        if log: log.info('FILE: %s: case %d/%d: %d engines' % (getattr(fi, 'name', type(fi).__name__), N-n, N, len(engines)))
        yield (len(engines), map2index(parser_queries(nl, require=0), engines))

def parser_engines(nl, require):
    n = int(nl().strip())
    assert n >= require, '%d < %d' % (n, require)
    if n < require:
        raise ValueError, '%d < %d' % (n, require)
    while n:
        n -= 1
        yield nl()[:-1] #.strip()

parser_queries = parser_engines

def map2index(it, index):
    d = {}
    for i in it:
        if not i in d:
            d[i] = index.index(i)
        yield d[i]

### time measurement

def timed(func, timer=None):
    """ decorates func() by logging execution time
    """
    funcname = getattr(func, '__name__', '?')

    if timer is None:
        import sys, time
        if sys.platform == "win32":
            # On Windows, the best timer is time.clock()
            timer = time.clock
        else:
            # On most other platforms the best timer is time.time()
            timer = time.time

    def timedfunc(*args, **kwargs):
        t0 = timer()

        try:
            r = func(*args, **kwargs)
        except:
            if log: log.info('TIME: %s: %g (ERROR)' % (funcname, timer()-t0))
            raise

        if log: log.info('TIME: %s: %g' % (funcname, timer()-t0))
        return r

    try:
        timedfunc.__name__ = func.__name__
    except:
        pass

    return timedfunc


### testing

def test(func, *args, **kwargs):
    """ tests runner

          * controllable via several kwargs that are not passed to func:

            - testlabel:        log label before test
            - testresult:       assert equal to result of func
            - testresults:      join using space, and assert equal to result of func
    """
    label    = kwargs.pop('testlabel', None)
    expected = kwargs.pop('testresult', ' '.join(map(str, kwargs.pop('testresults', [test]))))
        # shortcut hack: str(test) value implies no assertion was requested

    if label and log: log.info('TEST: %s' % label)

    result = func(*args, **kwargs)

    if expected != str(test):
        assert result == expected, result
    else:
        print result


### module execution

def one_arg_per_line(inp):
    return [eval(line) for line in inp.readlines() if line.strip()]

def main(run, parse=one_arg_per_line, log='', precompile=None):

    if not isinstance(log, logging.Logger):
        log = logging.getLogger(log)

    globals().update(log=log)

    from optparse import OptionParser
    optparser = OptionParser(
        usage="%prog [-dtTn] [FILELIST]",
        version="%prog 0.1")

    optparser.add_option("-d", "--debug",
        action="store_true",
        help="log debug messages")

    optparser.add_option("-t", "--timer",
        action="store_true",
        help="log execution time")

    optparser.add_option("-T", "--test",
        action="store_true",
        help="run doctests instead of processing input")

    optparser.add_option("-n", "--nocompile",
        action="store_false", default=True, dest="precompile",
        help="do not precompile functions using psyco")

    options, args = optparser.parse_args()

    if options.debug:
        log.setLevel(logging.DEBUG)
        # globals().update(debug=log.debug)
        from sys import stderr
        globals().update(debug=lambda message: stderr.write('# DEBUG:  %s\n' % message)) # much faster

    if options.precompile:
        try:
            import psyco
        except ImportError, e:
            log.warning('psyco not imported: %s' % e)

        if precompile is None:
            precompile = []
        elif not isinstance(precompile, list):
            precompile = list(precompile)
        precompile[0:0] = [run]

        log.info('precompiling using psyco: %s' % ', '.join([f.__name__ for f in precompile]))
        [psyco.bind(f) for f in precompile]

    if options.timer:
        run = timed(run)

    if options.test:
        globals().update(run=run, parse=parse)
        import doctest
        doctest.testmod()

    else:
        if args:
            import glob
            for gin in args:
                fins = glob.glob(gin)
                if not fins:
                    log.error("file/mask '%s' not found" % gin)
                else:
                    for fin in fins:
                        try:
                            fi = open(fin, 'rU')
                            print run(*parse(fi))
                            fi.close()
                        except:
                            log.exception("file '%s':" % fin)
        else:
            try:
                from sys import stdin
                print run(*parse(stdin))
            except:
                log.exception("file <stdin>:")


if __name__=='__main__':
    import logging
    logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)7s: %(message)s')

    main(results, parser, precompile=[])

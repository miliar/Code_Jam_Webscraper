""" Train Timetable

:Abstract: Solution to Google Code Jam 2008 practice problem.
:Authors:  iki
:Contact:  jan.killian at (g)mail.com

.. contents::

Problem statement
=================

A train line has two stations on it, A and B. Trains can take trips from A
to B or from B to A multiple times during a day. When a train arrives at B
from A (or arrives at A from B), it needs a certain amount of time before
it is ready to take the return journey - this is the turnaround time. For
example, if a train arrives at 12:00 and the turnaround time is 0 minutes,
it can leave immediately, at 12:00.

A train timetable specifies departure and arrival time of all trips between
A and B. The train company needs to know how many trains have to start the
day at A and B in order to make the timetable work: whenever a train is
supposed to leave A or B, there must actually be one there ready to go.
There are passing sections on the track, so trains don't necessarily arrive
in the same order that they leave. Trains may not travel on trips that do
not appear on the schedule.

Input
-----

The first line of input gives the number of cases, N. N test cases follow.

Each case contains a number of lines. The first line is the turnaround
time, T, in minutes. The next line has two numbers on it, NA and NB. NA is
the number of trips from A to B, and NB is the number of trips from B to A.
Then there are NA lines giving the details of the trips from A to B.

Each line contains two fields, giving the HH:MM departure and arrival time
for that trip. The departure time for each trip will be earlier than the
arrival time. All arrivals and departures occur on the same day. The trips
may appear in any order - they are not necessarily sorted by time. The hour
and minute values are both two digits, zero-padded, and are on a 24-hour
clock (00:00 through 23:59).

After these NA lines, there are NB lines giving the departure and arrival
times for the trips from B to A.

Output
------

For each test case, output one line containing "Case #x: " followed by the
number of trains that must start at A and the number of trains that must
start at B.

Limits
------

1 <= N <= 100

Small dataset

0 <= NA, NB <= 20

0 <= T <= 5

Large dataset

0 <= NA, NB <= 100

0 <= T <= 60


Doctest
=======

Problem sample:

>>> from cStringIO import StringIO
>>> test(run,
...   testlabel='sample (via parser)',
...   *parse(StringIO('''2
... 5
... 3 2
... 09:00 12:00
... 10:00 13:00
... 11:00 12:30
... 12:02 15:00
... 09:00 10:30
... 2
... 2 0
... 09:00 09:01
... 12:00 12:02
... ''')))
Case #1: 2 2
Case #2: 2 0


#>>> test(run, [[3, iter([0, 1, 0, 1, 0, 1])]],
#...   testlabel='3.1')
#Case #1: 0


"""

__docformat__ = 'restructuredtext en'

from heapq import heapify, heappop, heappush
from collections import deque
from itertools import izip, count
from string import maketrans

log = None
debug = None


### solution

def trains_needed(changes):
    times = sorted(changes.keys())
    r = s = 0
    for t in times:
        s += changes[t]
        if s < r:
            r = s
        if debug: debug('%02d:%02d %4d %4d (%d)' % (t/60, t%60, changes[t], s, -r))
    return -r

def results(it):
    return '\n'.join('Case #%d: %d %d' % (c, trains_needed(i[0]), trains_needed(i[1])) for i,c in izip(it, count(1)))

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
        if log: log.info('FILE: %s: case %d/%d' % (getattr(fi, 'name', type(fi).__name__), N-n, N))
        yield(parser_case(nl))

def parser_case(nl, require=0, min_t=0):
    t = int(nl().strip())
    if t < min_t:
        raise ValueError, '%d < %d' % (t, min_t)
    na,nb = map(int, nl().strip().split())
    if na < require:
        raise ValueError, '%d < %d' % (na, require)
    if nb < require:
        raise ValueError, '%d < %d' % (nb, require)

    if debug: debug('T:%2d  A->B:%3d B->A:%3d' % (t, na, nb))

    ca = {}
    cb = {}

    parse_table(nl, na, t, ca, cb)
    parse_table(nl, nb, t, cb, ca)

    return ca, cb

def parse_table(nl, n, t, lc, rc):
    while n:
        n -= 1
        o, i = map(hhmm2min, nl().strip().split())
        lc[o] = lc.get(o, 0) - 1
        i += t
        rc[i] = rc.get(i, 0) + 1

def hhmm2min(hhmm):
    h,m = map(int, hhmm.split(':'))
    return h * 60 + m

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

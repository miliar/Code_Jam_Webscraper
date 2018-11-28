""" Fly Swatter

:Abstract: Solution to Google Code Jam 2008 qualification
:Authors:  iki
:Contact:  jan.killian at (g)mail.com

.. contents::

Problem statement
=================

What are your chances of hitting a fly with a tennis racquet?

To start with, ignore the racquet's handle. Assume the racquet is a perfect
ring, of outer radius R and thickness t (so the inner radius of the ring is
R-t).

The ring is covered with horizontal and vertical strings. Each string is a
cylinder of radius r. Each string is a chord of the ring (a straight line
connecting two points of the circle). There is a gap of length g between
neighbouring strings. The strings are symmetric with respect to the center
of the racquet i.e. there is a pair of strings whose centers meet at the
center of the ring.

The fly is a sphere of radius f. Assume that the racquet is moving in a
straight line perpendicular to the plane of the ring. Assume also that the
fly's center is inside the outer radius of the racquet and is equally
likely to be anywhere within that radius. Any overlap between the fly and
the racquet (the ring or a string) counts as a hit.

.. image:: c.png

Input
-----

One line containing an integer N, the number of test cases in the input file.

The next N lines will each contain the numbers f, R, t, r and g separated
by exactly one space. Also the numbers will have at most 6 digits after the
decimal point.

Output
------

N lines, each of the form "Case #k: P", where k is the number of the test
case and P is the probability of hitting the fly with a piece of the
racquet.

Answers with a relative or absolute error of at most 10 ** -6 will be considered correct.

Limits
------

f, R, t, r and g will be positive and smaller or equal to 10000.

t < R

f < R

r < R

Small dataset

1 <= N <= 30

The total number of strings will be at most 60 (so at most 30 in each direction).

Large dataset

1 <= N <= 100

The total number of strings will be at most 2000 (so at most 1000 in each direction).


Doctest
=======

Problem sample:

>>> from cStringIO import StringIO
>>> test(run,
...   testlabel='sample (via parser)',
...   *parse(StringIO('''5
... 0.25 1.0 0.1 0.01 0.5
... 0.25 1.0 0.1 0.01 0.9
... 0.00001 10000 0.00001 0.00001 1000
... 0.4 10000 0.00001 0.00001 700
... 1 100 1 1 10
... ''')))
Case #1: 1.000000
Case #2: 0.910015
Case #3: 0.000000
Case #4: 0.002371
Case #5: 0.573972

"""

__docformat__ = 'restructuredtext en'

log = None
debug = None

from itertools import izip, count
from math import pi, sqrt, asin, cos


### solution - geometrical approach

def P(f, R, t, r, g):

    if g <= 2 * f:
        # < .. no fly fits between strings
        # = .. probability is still ->0
        return 1

    SR = pi * R**2 / 4   # area of rocket in Q1
    if debug: debug('SR = %16.6f' % SR)

    SF = 0               # area in Q1 that's safe for fly to have its center there
    s  = g - 2 * f       # safe inner square base
    s2 = s**2
    F  = R - t - f       # safe inner circle radius
    F2 = F**2

    x0 = r + f           # initial safe zone start on x axis
    x1 = x0 + s          # initial safe zone end on x axis
    d  = 2 * r + g       # difference between 2 safe zones (starts) on x axis

    if debug: debug('s  = %16.6f' % s)
    if debug: debug('d  = %16.6f' % d)
    if debug: debug('F  = %16.6f' % F)
    if debug: debug('s2 = %16.6f' % s2)

    while x1 < F:
        y0 = sqrt(F2 - x0**2)
        y1 = sqrt(F2 - x1**2)
        full_squares, h = full_items(y1, s, d, r+f)
        SF += full_squares * s2
        if debug: debug('SF + %4d * %16.6f = %16.6f  @  [%11.6f, %11.6f] [%11.6f, %11.6f]' % (full_squares, s2, SF, x0, y0, x1, y1))
        while h < y0:
            cut = square_cut_by_circle(F, x0, h, s, y0, y1)
            SF += cut
            if debug: debug('SF + %6s %16.6f = %16.6f  @  [%11.6f, %11.6f]' % ('', cut, SF, x0, h))
            h += d
        # could be further optimized: horizontal == vertical; both = 2*vertical - s*s
        x0 += d
        x1 += d

    if x0 < F:
        y0 = sqrt(F2 - x0**2)
        h = r + f
        while h < y0:
            cut = square_cut_by_circle(F, x0, h, s, y0, 0)
            SF += cut
            if debug: debug('SF + %6s %16.6f = %16.6f  @  [%11.6f, %11.6f]' % ('', cut, SF, x0, h))
            h += d

    return 1 - SF/SR

def square_cut_by_circle(r, x0, h, s, y0=None, y1=None):
    # est.: Q1, upper right corner outside, bottom left corner inside
    x1 = x0 + s

    if y0 is None:
        y0 = sqrt(r**2 - x0**2)
    if y1 is None:
        y1 = sqrt(r**2 - x1**2)

    if h+s > y0:
        # upper left corner outside

        if h > y1:
            # bottom right corner outside
            x2 = sqrt(r**2 - h**2)
            return circle_cut_by_line(r, x0, y0, x2, h, '---')  +  (x2 - x0) * (y0 - h) / 2
        else:
            # bottom right corner inside
            return circle_cut_by_line(r, x0, y0, x1, y1, '--2')  +  (x1 - x0) * (y1 - h)  +  (x1 - x0) * (y0 - y1) / 2
                # (x1 - x0) * ((y0 + y1) / 2 - h)
                # (x1 - x0) * (y1 - h)  +  (x1 - x0) * (y0 - y1) / 2
    else:
        # upper left corner inside
        y3 = h + s
        x3 = sqrt(r**2 - y3**2)

        if h > y1:
            # bottom right corner outside
            x2 = sqrt(r**2 - h**2)
            return circle_cut_by_line(r, x3, y3, x2, h, '4--')  +  (x3 - x0) * (y3 - h)  +  (x2 - x3) * (y3 - h) / 2
                # (y3 - h) * ((x2 + x3) / 2 - x0)
                # (x3 - x0) * (y3 - h)  +  (x2 - x3) * (y3 - h) / 2
        else:
            # bottom right corner inside
            return circle_cut_by_line(r, x3, y3, x1, y1, '4-2')  +  s**2  - (x1 - x3) * (y3 - y1) / 2


def circle_cut_by_line(r, x0, y0, x1, y1, typ='???'):
    c = sqrt((x1-x0)**2 + (y0-y1)**2) / 2
    fi = asin(c / r) * 2
    if debug: debug('%30s %16.6f %3s [%11.6f, %11.6f] [%11.6f, %11.6f] | %7.6f %11.6f' % \
        ('', r * (r * fi / 2 - c), typ, x0, y0, x1, y1, fi, c))
    return (r**2 * fi / 2) - (c * r * cos(fi/2))
        #  cut area (r**2 * fi / 2) - inner triangle (c * r * cos(fi))

def full_items(length, size, step, start=0):
    """ how many full items of size, with step between their centers, fill into length,
        and where starts the first that did not fit (may be > length)
    """
    length -= start
    c = int(length / step)
    n = c * step + start
    m = length - n
    if m >= size:
        c += 1
        n += step
    return c, n


def results(it):
    return '\n'.join('Case #%d: %0.6f' % (c, P(*i)) for i,c in izip(it, count(1)))


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
        f, R, t, r, g = map(float, nl().strip().split())
        if log: log.info('FILE: %s: case %d/%d:  f=%f R=%f t=%f r=%f g=%f' % (getattr(fi, 'name', type(fi).__name__), N-n, N, f, R, t, r, g))
        yield f, R, t, r, g


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

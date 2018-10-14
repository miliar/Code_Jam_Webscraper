#!/usr/bin/env python2.6

# Copyright Nate White, 2010

import optparse
import sys

def generate(options):
    import random
    # TODO Write sample input generator
    print options.generate
    for i in xrange(options.generate):
        A, B, C = (random.randint(1, 10 ** 50), random.randint(2, 1000),
                   random.randint(1, 10 ** 50))
        print A, B, C

def main():
    parser = optparse.OptionParser()
    parser.set_usage('%prog [options] <file>')
    parser.add_option("-d", "--debug", default=False,
        action="store_true", help="print progress messages to stdout")
    parser.add_option("-g", "--generate", default=None, action="store",
        type="int", metavar="N", help="generate a sample input of N tests")
    parser.add_option("-p", "--profile", default=False, action="store_true",
        help="run with profiling enabled")
    parser.add_option("-v", "--verify", default=False, action="store_true",
        help="verify result using brute force algorithm")
    (options, args) = parser.parse_args()
    if len(args) != 0:
        print parser.error('Unexpected positional arguments seen')

    if options.generate:
        generate(options)
        return

    if options.profile:
        import cProfile as profile
        profile.runctx("puzzle(options, args)", globals(), locals())
    else:
        puzzle(options, args)

def brute(options, n):
    return 0 # TODO Write brute-force solver

def solve(options, A1, A2, B1, B2):
    return (A2 - A1 + 1) * (B2 - B1 + 1)
    return 0 # TODO Write production solver

def play(a, b):
    # Return true if player 1 wins
    turn = True
    while True:
        if a == b:
            return not turn
        if a > b:
            a, b = b, a
        if (a, b) in known:
            return known[(a, b)] ^ turn
        turn = not turn

known = {}

def playr(a, b):
    #if (a,b) in known:
    #    return known[(a,b)]
    if a > b:
        a, b = b, a
    if a == 0 or b == 0 or a == b:
        return False
    if a == 1 or b == 1:
        return True
    d = b / a
    res = not playr(a, b - a * d)
    while d > 1:
        if not res and not playr(a, b - a * (d - 1)):
            res = True
        d -= 1
    return res

def puzzle(options, args):
    #N = 30
    #for i in xrange(1, N):
    #    for j in xrange(1, N):
    #        print 'T' if playr(i, j) else 'F',
    #    print
    #return
    (N,) = ([int(i) for i in sys.stdin.readline().split()])
    for n in xrange(1, N + 1):
        res = 0
        (A1,A2,B1,B2) = ([int(i) for i in sys.stdin.readline().split()])
        #res = solve(options, A1, A2, B1, B2)
        for i in xrange(A1, A2 + 1):
            for j in xrange(B1, B2 + 1):
                if playr(i, j):
                    res += 1
        if options.verify:
            res2 = brute(options, n)
            if options.debug:
                print "Production solution", res, "vs. brute-force", res2
            assert res == res2
        print 'Case #%d: %d' % (n, res)

if __name__ == '__main__':
    main()

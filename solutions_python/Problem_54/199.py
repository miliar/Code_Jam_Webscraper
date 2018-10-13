#!/usr/bin/env python2.6

# Copyright Nate White, 2010

import optparse
import sys

def generate(options):
    import random
    print options.generate
    for i in xrange(options.generate):
        GCD, N, A = (random.randint(1, 10 ** 50), random.randint(2, 1000),
                     random.randint(1, 10 ** 50))
        if options.debug:
            print >> sys.stderr, GCD, A
        print N,
        for n in xrange(N):
            print random.randint(1, 10000) * GCD + A,
        print

def gcd(l):
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        a, b = l[0], l[1]
        r = min(a, b)
        while r:
            if a == r:
                b %= r
            else:
                assert b == r
                a %= r
            r = min(a, b)
        res = a or b
        assert l[0] % res == 0
        assert l[1] % res == 0
        return res

    r = gcd([l[0], l[1]])
    for i in l[1:]:
        r = gcd([r, i])
    return r

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
        help="roughly verify result using divisions")
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

def puzzle(options, args):
    (C,) = ([int(i) for i in sys.stdin.readline().split()])
    for c in xrange(1, C + 1):
        l = ([int(i) for i in sys.stdin.readline().split()])
        N = l[0]
        l = l[1:N + 1]
        diffs = [0] * (N - 1)
        for i in xrange(N - 1):
            diffs[i] = abs(l[i + 1] - l[i])

        # Compute GCD of all pairwise time differences
        diffs = [i for i in diffs if i != 0]
        maybe = gcd(diffs)
        if options.debug:
            print "GCD?", maybe
        rem = l[0] % maybe
        for i in l:
            #print rem, i, maybe, i % maybe
            assert i % maybe == rem

        res = (maybe - rem) % maybe
        for t in l:
            assert (t + res) % maybe == 0
        if options.verify:
            div = [(t + res) / maybe for t in l]
            assert gcd(div) == 1

        print 'Case #%d: %d' % (c, res)

if __name__ == '__main__':
    main()

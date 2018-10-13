#!/usr/bin/env python2.6

# Copyright Nate White, 2010

import optparse
import sys

def main():
    parser = optparse.OptionParser()
    parser.set_usage('%prog [options] <file>')
    parser.add_option("-d", "--debug", default=False,
        action="store_true", help="print progress messages to stdout")
    parser.add_option("-p", "--profile", default=False, action="store_true",
        help="run with profiling enabled")
    (options, args) = parser.parse_args()
    if len(args) != 0:
        print parser.error('Unexpected positional arguments seen')

    if options.profile:
        import cProfile as profile
        profile.runctx("puzzle(options, args)", globals(), locals())
    else:
        puzzle(options, args)

def puzzle(options, args):
    (T,) = ([int(i) for i in sys.stdin.readline().split()])
    for t in xrange(1, T + 1):
        (N, K) = ([int(i) for i in sys.stdin.readline().split()])
        print 'Case #%d: %s' % (t, "ON" if K & (2 ** N - 1) == (2 ** N - 1) else "OFF")

if __name__ == '__main__':
    main()

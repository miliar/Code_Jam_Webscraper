#!/usr/bin/env python

import sys

def main(in_stream, out_stream):
    n_cases = int(in_stream.next())
    for idx in xrange(1, n_cases+1):
        a, b, k = map(int, in_stream.next().split())
        res = sum(i & j < k for i in xrange(a) for j in xrange(b))
        out_stream.write('Case #%d: %d\n' % (idx, res))

if __name__ == '__main__':
    main(sys.stdin, sys.stdout)

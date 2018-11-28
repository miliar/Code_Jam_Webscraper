#!/usr/bin/env python
import sys


def log(fmt, *args):
    sys.stderr.write((fmt + '\n') % args)

def read_int():
    return int(raw_input())

def read_ints():
    return [int(s) for s in raw_input().split()]


def do_case():
    def rotate(s):
        return s[-1] + s[:-1]

    A, B = read_ints()
    pairs = set()

    for n in xrange(A, B):
        nstr = str(n)
        mstr = rotate(nstr)
        while nstr != mstr:
            if mstr[0] != '0':
                m = int(mstr)
                if n < m <= B:
                    pairs.add((n, m))
            mstr = rotate(mstr)
    
    return len(pairs)


if __name__ == '__main__':
    for case in xrange(read_int()):
        print 'Case #%d: %s' % (case + 1, do_case())

#!/usr/bin/env python

import sys

def permute(sequence):
    if len(sequence) == 0:
        yield ()
    else:
        for i in xrange(0, len(sequence)):
            for rest in permute(sequence[:i] + sequence[i + 1:]):
                yield (sequence[i],) + rest

def main():
    T = int(raw_input())
    for blah in range(T):
        N = raw_input()
        iN = int(N)
        perm = [int(''.join(s)) for s in permute(N)]
        perm.sort()
        if iN >= perm[-1]:
            N = N + '0'
            perm = [int(''.join(s)) for s in permute(N)]
            perm.sort()
            for i in perm:
                if i > iN:
                    print 'Case #%d: %d' % (blah + 1, i)
                    break
        else:
            for i in perm:
                if i > iN:
                    print 'Case #%d: %d' % (blah + 1, i)
                    break

if __name__ == '__main__':
    main()


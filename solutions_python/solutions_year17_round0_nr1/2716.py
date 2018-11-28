#!/usr/bin/python

import sys


if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = [l[:-1] for l in f.readlines()]

    outlines = []

    for i, line in enumerate(lines[1:]):
        s, k = line.split(' ')
        k = int(k)
        l = len(s)
        b = eval('0b' + ''.join(['1' if v == '-' else '0' for v in s]))
        kmask = 2**k - 1
        iter = 0
        while b > 0:
            lsb = (b & -b).bit_length() - 1
            b ^= kmask << lsb
            iter += 1
            if lsb > l - k:
                break
        if b != 0:
            iter = 'IMPOSSIBLE'

        outlines.append('Case #%s: %s' % (i + 1, iter))

    fname = fname[:-2] + 'out'
    with open(fname, 'w') as f:
        f.write('\n'.join(outlines))

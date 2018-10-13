#!/usr/bin/python

import sys


if __name__ == '__main__':

    fname = sys.argv[-1]
    with open(fname, 'r') as f:
        lines = [l[:-1] for l in f.readlines()]

    outlines = []

    for i, line in enumerate(lines[1:]):
        out = []
        pos = -1
        iline = [int(v) for v in line]
        d_pre = iline[-1]
        for j,d in enumerate(iline[:-1][::-1]):
            if d > d_pre:
                pos = j + 1
                d_pre = d - 1
            else:
                d_pre = d

        if pos >= 0:
            out = iline[:-pos-1] + [iline[-pos-1] - 1] + [9] * pos
        else:
            out = iline

        iout = int(''.join([str(v) for v in out]))

        outlines.append('Case #%s: %s' % (i + 1, iout))

    fname = fname[:-2] + 'out'
    with open(fname, 'w') as f:
        f.write('\n'.join(outlines))

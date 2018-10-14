from __future__ import print_function
from __future__ import division
import sys
#from itertools import izip, ifilter, imap
#from collections import defaultdict

import gcj_util
from gcj_util import (
    dprint,
    read_ints,
    read_floats,
    read_int,
)


def solve(capacity, files):
    files.sort(reverse=True)
    discs = [0] * len(files)
    nfiles = [0] * len(files)
    ndiscs = 0

    for size in files:
        for i in range(len(discs)):
            if discs[i] == 0:
                discs[i] = size
                nfiles[i] += 1
                ndiscs += 1
                break
            if nfiles[i] < 2 and capacity - discs[i] >= size:
                nfiles[i] += 1
                discs[i] += size
                break

    return ndiscs

def read_case(fp):
    nfiles, capacity = read_ints(fp)
    files = read_ints(fp)
    assert len(files) == nfiles
    return capacity, files


def write_result(fp, casenum, result):
    fp.write('Case #%d: %s\n' % (casenum, result))
    fp.flush()


def read_cases(fp):
    T = read_int(fp)
    for i in range(T):
        yield read_case(fp)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        gcj_util.DEBUG = True

    in_fp = sys.stdin
    out_fp = sys.stdout
    for casenum, case in enumerate(read_cases(in_fp)):
        result = solve(*case)
        write_result(out_fp, casenum + 1, result)

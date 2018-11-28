# -*- coding: utf-8 -*-
# This library is available online and free to use:
# https://github.com/yanatan16/pycodejam
from codejam.parsers import iter_parser

import itertools
import numpy as np


def solve(*lines):
    N, lines = lines
    counts_list = []
    basic_fp = None
    steps = 0
    for line in lines:
        fp = []
        counts = []
        for ch, group in itertools.groupby(line):
            fp.append(ch)
            counts.append(sum(1 for _ in group))
        fp = ''.join(fp)
        if basic_fp is None:
            basic_fp = fp
        else:
            if fp != basic_fp:
                return "Fegla Won"
        counts_list.append(counts)
    counts = np.array(counts_list, dtype='int')
    for i in xrange(len(basic_fp)):
        slice = counts[:, i]
        mean = int(round(slice.mean()))
        steps += sum(abs(el - mean) for el in slice)
    return steps


@iter_parser
def parse(nxtline):
    N = int(nxtline())
    return N, [nxtline() for _ in xrange(N)]


if __name__ == "__main__":
    from codejam import CodeJam
    CodeJam(parse, solve).main()

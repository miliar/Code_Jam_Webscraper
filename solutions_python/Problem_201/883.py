# Python 3.5.1

from common import *

def main(casenum):
    n, k = readints()
    gaps = {n : 1}

    while True:
        m = max(gaps.keys())
        count = gaps[m]
        a = m // 2
        b = (m - 1) // 2

        if k <= count:
            writecase(casenum, '{} {}'.format(a, b))
            break

        del gaps[m]
        if a not in gaps:
            gaps[a] = 0
        if b not in gaps:
            gaps[b] = 0
        gaps[a] += count
        gaps[b] += count
        k -= count

run(main)

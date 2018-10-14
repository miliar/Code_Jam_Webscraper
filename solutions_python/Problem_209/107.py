import sys
import math

f = sys.stdin

if 'DEBUG' in sys.argv:
    f = open('in.txt', 'r')


def circ_len(p):
    return 2.0 * p.r * math.pi


def top_area(p):
    return math.pi * (p.r ** 2)


def maxSyrup(pancackes, k):
    assert pancackes

    p0 = pancackes[0]
    result = top_area(p0) + circ_len(p0) * p0.h

    if len(pancackes) == 1:
        return result

    sideArs = [circ_len(p) * p.h for p in pancackes[1:]]
    sideArs.sort()
    sideArs.reverse()
    k = min(k-1, len(sideArs))
    result += sum(sideArs[:k])
    return result


def findBestSet(pancackes, k):
    pnc = list(pancackes)
    pnc.sort(key=lambda p: -p.r)
    res = []
    for start in range(len(pnc)):
        res.append(maxSyrup(pnc[start:], k))
    return max(res)


class Pancacke(object):
    def __init__(self, r, h):
        self.r = r
        self.h = h


def gi():
    return int(f.readline())


def gil():
    return map(int, f.readline().strip().split())


def solve():
    tests = gi()
    for testNr in range(1, tests + 1):
        n, k = gil()
        pcs = []
        for _ in range(n):
            r, h = gil()
            pcs.append(Pancacke(r, h))
        res = findBestSet(pcs, k)
        print "Case #%d: %.10f" % (testNr, res)


solve()

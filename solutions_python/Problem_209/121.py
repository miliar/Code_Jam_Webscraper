from __future__ import division
from math import pi


def reader(in_file):
    n, k = in_file.get_ints()
    pans = []
    for _ in xrange(n):
        pans.append(in_file.get_ints())
    return n, k, pans


def cal(pans):
    res = pans[0][0] ** 2 * pi
    for pan in pans:
        res += pan[0] * pan[1] * 2 * pi
    return res

def solver((n, k, pans)):
    sides = []
    for i, pan in enumerate(pans):
        sides.append((pan[0], pan[1], 2 * pan[0] * pan[1], i))

    sides.sort(key= lambda x : -x[2])
    max_rad = max(sides[:k], key= lambda x:x[0])[0]

    best = 0

    for i, pan in enumerate(pans):
        if pan[0] < max_rad:
            continue
        res = [pan]
        if not len(res) == k:
            for side in sides:
                if side[3] == i:
                    continue
                res.append(side)
                if len(res) == k:
                    break

        thln = cal(res)
        best = max(thln, best)

    return best

if __name__ == "__main__":
    # GCJ library publicly available at http://ideone.com/2PcmZT
    from GCJ import GCJ
    GCJ(reader, solver, "a", "A").run()

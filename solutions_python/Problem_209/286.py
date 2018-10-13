from __future__ import division

from math import floor, ceil

import math

# f_name = 'sample.in'
# f_name = 'A-small-attempt0.in'
f_name = 'A-large.in'

f_out_name = f_name[:-2] + 'out'


def parse_input(str_test):
    t = str_test.split()
    n = map(int, t)
    return n


def solve(N, K, R, H):
    s = 0
    for i, ri in enumerate(R):
        S = math.pi * ri ** 2 + math.pi * ri * 2 * H[i]
        hr = [(h, r) for (j,(h, r)) in enumerate(zip(H, R)) if r <= ri and j != i]
        if len(hr) < K - 1:
            continue
        HS = map(lambda (h, r): math.pi * r * 2 * h, hr)
        si = sum(sorted(HS, reverse=True)[:K - 1])
        s = max(s,si + S)
    return str(s)


with open(f_name) as f_in, open(f_out_name, 'w') as f_out:
    T = int(f_in.readline())
    for i in xrange(T):
        N, K = map(int, f_in.readline().split())
        R = []
        H = []
        for j in xrange(N):
            Ri, Hi = map(int, f_in.readline().split())
            R.append(Ri)
            H.append(Hi)
        out = solve(N, K, R, H)
        f_out.write('Case #{0}: {1}\n'.format(i + 1, out))

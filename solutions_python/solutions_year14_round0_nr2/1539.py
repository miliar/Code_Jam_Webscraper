from __future__ import print_function
import sys
import math

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")


T = int(f.readline().strip())

for case_id in range(1, T+1):
    C, F, X = map(float, f.readline().strip().split())

    j_lo = math.floor(X/C - 1 - 2.0/F)
    j_hi = math.ceil(X/C - 2.0/F)
    #~ print(j_lo, j_hi)

    k = 0
    if j_lo >= 0 and j_lo + 1 < j_hi:
        k = int(j_lo + 1)

    t = C*math.fsum([1.0/(2.0+i*F) for i in xrange(0, k+1)]) + (X-C)/(2.0+k*F)

    r = str.format('{0:.7f}', t)
    print(str.format('Case #{0}: {1}', case_id, r))

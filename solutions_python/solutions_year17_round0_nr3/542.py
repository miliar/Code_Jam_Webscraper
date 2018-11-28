import sys
from fractions import gcd
import numpy as np

lines = open(sys.argv[1]).readlines()

T = int(lines[0])

casenum = 0

for line in lines[1:]:
    casenum += 1
    vals = line.split()
    N = int(vals[0])
    K = int(vals[1])

    #print N, K

    binK = '{0:b}'.format(K)
    bits = len(binK)

    bin_pos = long('0' + binK[1:],2)

    bin_size = 2**(bits-1)

    stalls_in_bin = N - 2**bits + 1

    bin_low = stalls_in_bin / (2*bin_size)
    num_highs = stalls_in_bin - 2 * bin_size * bin_low

    lo = hi = bin_low

    if bin_pos < num_highs:
        hi = bin_low + 1
    if bin_pos < num_highs - bin_size:
        lo = bin_low + 1

    print 'case #' + str(casenum) + ": " + str(hi) + ' ' + str(lo)


        

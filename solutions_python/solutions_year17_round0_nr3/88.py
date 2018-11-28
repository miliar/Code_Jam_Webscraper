import numpy as np
from math import log2, ceil, floor
from functools import lru_cache

def smallest_gap(n, k):
    n_bins = 1 << (floor(log2(k)) + 1)
    small_bin_size = floor(n/n_bins)
    large_bin_size = ceil(n/n_bins)
    num_large_bins = n - (n_bins * small_bin_size)

@lru_cache(maxsize=None)
def smallest_gap_recursive(n, k):
    r = (n - 1) / 2
    if k == 1:      # Base case:  One guy --> Take the center stall
        return (ceil(r), floor(r))

    s = ceil((k -1) / 2)
    if ((n-1) % 2) and ((k-1) % 2):
        return smallest_gap_recursive(ceil(r), s)
    else:
        return smallest_gap_recursive(floor(r), s)


if __name__=='__main__':
    PATH_IN = 'C-small-2-attempt0.in'
    PATH_OUT = PATH_IN[:-3] + '.out'

    f_in = open(PATH_IN, 'r')
    f_out = open(PATH_OUT, 'w')

    T = next(f_in)
    for i, line in enumerate(f_in):
        print(line.strip())

        n, k = line.split()
        n = int(n)
        k = int(k)

        res = '%i %i' % smallest_gap_recursive(n, k)

        print('Case #%i: %s' % (i+1, res))
        print()
        f_out.write('Case #%i: %s\n' % (i+1, res))

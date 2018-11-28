from __future__ import print_function

import sys

fin = sys.stdin

num_cases = int(fin.readline().strip())

for t in range(num_cases):
    R,C,W = [int(x) for x in fin.readline().split()]
    tries = (R-1) * (C // W) # other rows
    tries += (C // W) # in target row
    if C % W != 0:
        tries += 1
    tries += W - 1
    print("Case #{}: {}".format(t+1, tries))
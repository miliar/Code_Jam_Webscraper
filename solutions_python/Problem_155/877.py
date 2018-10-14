from __future__ import print_function
import sys

f = sys.stdin

if len(sys.argv) > 1:
    f = open(sys.argv[1], "rt")

T = int(f.readline().strip())

for case_id in range(1, T+1):
    S_max, values_str = f.readline().strip().split()

    num_added = 0
    num_standing = 0

    for i, d in enumerate(values_str):
        k = int(d)
        if num_standing >= i:
            num_standing += k
        else:
            a = i - num_standing
            num_added += a
            num_standing = i + k

    r = num_added
    print(str.format('Case #{0}: {1}', case_id, r))

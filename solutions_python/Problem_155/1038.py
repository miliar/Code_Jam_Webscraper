from __future__ import print_function

import sys

fin = sys.stdin

num_cases = int(fin.readline().strip())

for c in range(num_cases):
    _, s = fin.readline().split()
    standing = 0
    friends = 0
    for i, n in enumerate(s):
        n = int(n)
        if n == 0:
            continue

        if standing < i:
            friends += i - standing
            standing = i

        standing += n

    print("Case #{}: {}".format(c+1, friends))

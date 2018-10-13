from __future__ import print_function

import collections
import math
import numpy as np
import sys

def solve(s, k):
    n = len(s)
    a = np.zeros(n, dtype=bool)
    for i in range(n):
        if s[i] == '+':
            a[i] = True
    ret = 0
    for i in range(n - k + 1):
        if not a[i]:
            ret += 1
            for j in range(i, i + k):
                a[j] = not a[j]
    if not np.all(a[(n-k+1):n]):
        return "IMPOSSIBLE"
    return ret

if __name__ == "__main__":
    line = sys.stdin.readline() # (Note: keeps final newline)
    #print('<', line, '>', sep='')
    T = int(line)
    for no in range(1, T+1):
        print(no, "/", T, file=sys.stderr)

        # Read input for this case
        #for line in sys.stdin:
        line = sys.stdin.readline()
        ### Pass string, stripping whitespace (i.e. newline) from the end:
        a, b = line.split()
        b = int(b)
        ### Read one integer:
        #a = int(line)
        ### Read fixed number of integers:
        #a, b = (int(val) for val in line.split())
        ### Read list of integers:
        #a = [int(val) for val in line.split()]

        ret = solve(a, b)

        # Write output
        ### Without formatting:
        print("Case #", no, ": ", ret, sep='')
        ### Print elements of sequence separated by spaces:
        #if not type(ret) is list:
        #    print("Warning: ret is not a list", file=sys.stderr)
        #print("Case #", no, ": ", " ".join(map(str, ret)), sep='')
        ### Print multiple lines
        #print("Case #", no, ":", sep='')
        #rets = ret
        #for ret in rets:
        #    print(" ".join(map(str, ret)))

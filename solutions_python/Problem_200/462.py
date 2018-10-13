from __future__ import print_function

import collections
import math
import numpy as np
import sys

def solve(s):
    a = []
    for c in s:
        a.append(int(c))
    n = len(a)
    for i in range(1, n):
        if a[i-1] > a[i]:
            i2 = i - 1
            while i2 > 0 and a[i2-1] == a[i-1]:
                i2 -= 1
            a[i2] -= 1
            for j in range(i2+1, n):
                a[j] = 9
            break
    ret = 0
    for d in a:
        ret *= 10
        ret += d
    #print(s, file=sys.stderr)
    #print(ret, file=sys.stderr)
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
        a = line.rstrip()
        ### Read one integer:
        #a = int(line)
        ### Read fixed number of integers:
        #a, b = (int(val) for val in line.split())
        ### Read list of integers:
        #a = [int(val) for val in line.split()]

        ret = solve(a)

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

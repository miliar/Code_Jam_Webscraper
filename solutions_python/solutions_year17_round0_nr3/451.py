from __future__ import print_function

import collections
import math
import numpy as np
import sys

def solve(n, k):
    a = [[n, 1]]
    k -= 1
    i = 0
    while k >= a[i][1]:
        cursize = a[i][0]
        curnum = a[i][1]
        k -= a[i][1]
        i += 1
        addsize = (int)((cursize) / 2)
        if a[-1][0] == addsize:
            a[-1][1] += curnum
        else:
            a.append([addsize, curnum])
        addsize = (int)((cursize - 1) / 2)
        if a[-1][0] == addsize:
            a[-1][1] += curnum
        else:
            a.append([addsize, curnum])
    cursize = a[i][0]
    ret_max = (int)((cursize) / 2)
    ret_min = (int)((cursize - 1) / 2)
    return "{0} {1}".format(ret_max, ret_min)

if __name__ == "__main__":
    #print(sys.maxint)
    line = sys.stdin.readline() # (Note: keeps final newline)
    #print('<', line, '>', sep='')
    T = int(line)
    for no in range(1, T+1):
        print(no, "/", T, file=sys.stderr)

        # Read input for this case
        #for line in sys.stdin:
        line = sys.stdin.readline()
        ### Pass string, stripping whitespace (i.e. newline) from the end:
        #a = line.rstrip()
        ### Read one integer:
        #a = int(line)
        ### Read fixed number of integers:
        a, b = (int(val) for val in line.split())
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

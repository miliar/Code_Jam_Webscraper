#! /usr/bin/python3.1

import sys
from sys import stdin
import os

def solve(n, k):
    m = 1 << n
    return (k % m) == (m - 1)

def main(argv=sys.argv):
    ncases = int(stdin.readline().strip())
    cases = []
    for i in range(1, ncases + 1):
        n, k = [int(x) for x in stdin.readline().split()]
        result = "ON" if solve(n, k) else "OFF"
        print("Case #{0}: {1}".format(i, result))
    return 0
        
if __name__ == '__main__':
    sys.exit(main())

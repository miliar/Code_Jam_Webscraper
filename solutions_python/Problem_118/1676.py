#!/usr/bin/env python

import math
import copy

fs_numbers = [1,
              4,
              9,
              121,
              484,
              10201,
              12321,
              14641,
              40804,
              44944,
              1002001,
              1234321,
              4008004,
              100020001,
              102030201,
              104060401,
              121242121,
              123454321,
              125686521,
              400080004,
              404090404,
              10000200001,
              10221412201,
              12102420121,
              12345654321,
              40000800004,
              1000002000001,
              1002003002001,
              1004006004001,
              1020304030201,
              1022325232201,
              1024348434201,
              1210024200121,
              1212225222121,
              1214428244121,
              1232346432321,
              1234567654321,
              4000008000004,
              4004009004004,
              100000020000001]

def ispalindrome(n):
    n = int(n)
    s = [c for c in str(n)]
    srev = copy.deepcopy(s)
    srev.reverse()
    return s == srev

def is_fs(n):
    sr = math.sqrt(n)
    if sr == int(sr):
        r = ispalindrome(n) and ispalindrome(sr)
        return r
    else:
        return False

def find_fs(lo, hi):
    return len(filter(is_fs, range(lo, hi+1)))

# generate all fair & square numbers from 1 to n
def gen_fs(n):
    l = []
    for i in xrange(n):
        sq = i * i
        if sq > n:
            break
        if ispalindrome(i) and ispalindrome(sq):
            l.append(sq)
    return l

def main():
    import sys
    if len(sys.argv) < 2:
        return 'usage: fs.py filename'
        exit(1)
    filename = sys.argv[1]
    f = open(filename)
    firstline = True
    numcases = 0
    intervals = []
    for line in f:
        if firstline:
            numcases = int(line)
            firstline = False
            continue
        intervals.append(map(int, line.split(' ')))
    i = 1
    for ival in intervals:
        lo, hi = ival[0], ival[1]
        result = 0
        for n in fs_numbers:
            if n >= lo and n <= hi:
                result += 1
        print 'Case #{}: {}'.format(i, result)
        i += 1

if __name__ == '__main__':
    main()

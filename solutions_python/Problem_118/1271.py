#!/usr/bin/python


import sys
from itertools import izip


good_nums = [1, 4, 9, 121, 484]


def count(A, B):
    l = 0
    h = 4
    while good_nums[l] < A:
        if l == 4:
            return 0
        l += 1
    while good_nums[h] > B:
        if h == 0:
            return 0
        h = h - 1
    return h - l + 1


def main():
    fin_file = sys.argv[1]
    
    with open(fin_file, 'r') as fin:
        T = int(fin.readline().strip())
        
        for t in xrange(T):
            line = fin.readline().strip()
            A, B = map(int, line.split(" "))
            print "Case #%d: %d" % ((t + 1), count(A, B))

        
if __name__ == '__main__':
    main()
    
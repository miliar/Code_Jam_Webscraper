#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools, collections
import sys
import math
import fractions
import string

def input_read(filename):
    data = None
    with open(filename) as f:
        for x in f:
            yield [int(s.strip()) for s in x.split()]

def output_file(filename, ans):
    with open(filename, 'w') as f:
        for n, a in enumerate(ans,1):
            f.write('Case #%d:' % n)
            if a: 
                f.write(' YES')
            else:
                f.write(' NO')
            f.write('\n')
    return

def gen_testcase(ifilename):
    itr = input_read(ifilename)
    [T] = next(itr)
    for x in range(T):
        lawn = list()
        r, c = next(itr)
        for x in range(r):
            lawn.append(next(itr))
        yield r, c, lawn

def solve_one(y, x, lawn):
    print('size: %d x %d' % (x, y))
    #print(lawn)
    for idy in range(y):
        for idx in range(x):
            cur = lawn[idy][idx]
            if not check_row(cur, lawn, idy):
                if not check_col(cur, lawn, idx, y):
                    return False
    return True

def check_row(cur, lawn, idy):
    for val in lawn[idy]:
        if val > cur:
            return False
    return True

def check_col(cur, lawn, idx, ysize):
    for y in range(ysize):
        if lawn[y][idx] > cur:
            return False
    return True

def solve_all(inputfile):
    for r, c, lawn in gen_testcase(inputfile):
         yield solve_one(r, c, lawn)

def main(ifile, ofile):
    output_file(ofile, solve_all(ifile))
    return

if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    #parser.add_option('-i', type='string', dest='ifile', help='input filename', default='input.txt')
    parser.add_option('-o', type='string', dest='ofile', help='output filename', default='output.txt')
    
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        sys.exit()

    try:
        main(args[0], options.ofile)
    except IOError as data:
        print(data)


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
            f.write('Case #%d: %d\n' % (n, a))
    return

def gen_testcase(ifilename):
    itr = input_read(ifilename)
    [T] = next(itr)
    for x in range(T):
        yield next(itr)

def solve_one(vrange):
    print(vrange)
    num = 0
    for val in range(vrange[0], vrange[1] + 1):
        if (is_palindrome(val)):
            #print('%s is palindrome' % val)
            tmp  = pow(val, 1/2)
            rnum = math.ceil(tmp)
            if rnum ** 2 != val:
                rnum = math.floor(tmp)
            if rnum ** 2 != val:
                continue

            if (is_palindrome(rnum)):
                print('%s is fair and square' % val)
                num += 1
        else:
            continue
    return num

def is_palindrome(num):
    s = str(num)
    length = len(s)
    i = 0
    for l, r in zip(s, reversed(s)):
        i += 1
        if (l == r):
            if (i > length // 2) :
                return True
            continue
        else:
            return False

def solve_all(inputfile):
    for field in gen_testcase(inputfile):
         yield solve_one(field)

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


#!/usr/bin/env python

import sys
import itertools

cache = {}
#ncache_hit = 0

def open_input(file):
    try:
        f = open(file, "r")
        return f
    except:
        print "can not open ", file
        sys.exit(1)

def make_denom(length):
    denom = '1'
    for i in range(length-1):
        denom += '0'
    return int(denom)

def make_recycled(num, length):
    ret = [] 
    multi = 10
    for l in range(length, 0, -1):
        denom = make_denom(l)
        recycle = num/denom + (num%denom * multi)
        ret.append(recycle)
        multi *= 10
    return ret

def do_solve(a, b, length):
    count = 0
    recycled_pairs = []
    for n in range(a, b):
        if n in cache:
            recycled = cache[n]
            #ncache_hit += 1
        else:
            recycled = make_recycled(n, length)
            cache[n] = recycled

        for r in recycled:
            if n < r <= b:
                recycled_pair = (n, r)
                if recycled_pair not in recycled_pairs:
                    recycled_pairs.append(recycled_pair)
                    count += 1
    return count

def solve(input):
    """ T = # test case """
    T = int(input.readline())

    """ line = A, B """
    for i in range(T):
        line = input.readline().rstrip()
        A, B = line.split()
        length = len(A)
        A = int(A)
        B = int(B)
        print "Case #{0}: {1}".format(i+1, do_solve(A, B, length))

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        solve(open_input(sys.argv[1]))
        #print "cache hit count: {0}".format(ncache_hit)
    else:
        print 'require input'
        sys.exit(1)

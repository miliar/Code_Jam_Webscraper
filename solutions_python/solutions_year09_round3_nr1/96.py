#!/usr/bin/env python

"""Google Code Jam 2009, Qualification round."""

import sys

def calc_res(data):
    d = {}
    first = data[0]
    idx = 0
    res = long(0)
    for i in data:
        if not d.has_key(i):
            d[i] = idx
            idx += 1
    min_base = len(d.keys())
    if min_base == 1:
        min_base = 2
    d[first] = 1 #can't start with 0
    idx = 1
    while idx < len(data) and data[idx] == first:
        idx += 1
    if idx < len(data) and data[idx] != first:
        d[data[idx]] = 0
    for digit in data:
        res = res*min_base + d[digit]
    return res

def main(args):
    if len(args) < 2:
        return 1
    try:
        f = open(args[1])
        #READ appropriate args from initial lines
        num_cases = int(f.readline())
        for case in xrange(num_cases):
            data = f.readline().strip()
            #CALCULATE answer for this case
            print "Case #" + str(case+1) + ": " + str(calc_res(data))
    except IOError:
        print "Invalid file input"
        return 2

if __name__ == '__main__':
    sys.exit(main(sys.argv))

#! /usr/bin/env python

import sys

first = lambda (x, y) : x
second = lambda (x, y) : y

class GError(Exception) :
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def shift_right(num, disp) : 
    nstr = str(num)
    pos = len(nstr) - disp
    return int(nstr[pos:] + nstr[:pos])

def shift_left(num, disp) : 
    nstr = str(num)
    return int(nstr[disp:] + nstr[:disp])

def bfsearch(floor, roof) :
    depth = len(str(roof)) 
    if depth <= 1 : return 0
    recnum = []
    count = 0
    for n in range(floor, roof+1) : 
        rec_n = set()
        for i in  range(1, depth) : 
            m = shift_left(n, i)
            if (m >= floor) & (m <= roof) & (m > n): 
                rec_n.add(m)
        if len(rec_n) != 0: 
            recnum.append((n, rec_n))
            count = count + len(rec_n)
    return count

def optsearch(floor, roof) :
    depth = len(str(roof)) 
    c = str(roof)[0]
    if depth <= 1 : return 0
    recnum = []
    count = 0
    idx = range(1, depth)
    for n in range(floor, roof+1) : 
        nstr = str(n)
        rec_n = set()
        for i in  range(1, depth) : 
            if nstr[i] > c: continue
            m = shift_left(n, i)
            if (m >= floor) & (m <= roof) & (m > n): 
                rec_n.add(m)
        if len(rec_n) != 0: 
            recnum.append((n, rec_n))
            count = count + len(rec_n)
    return count

if len(sys.argv) <= 0 : sys.exit()

fname = sys.argv[1] 
fh = open (fname) 

case_count = int(fh.readline().strip())

for i in range(1, case_count+1) :
    nums = map(int, fh.readline().split())
    floor = nums[0]
    roof = nums[1]
    print "Case #%d: %d" % (i, optsearch(floor, roof))
    
fh.close()

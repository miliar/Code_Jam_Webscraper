# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/zangetsu/.spyder2/.temp.py
"""

from __future__ import division;
from bisect import *;
import sys;
from math import *;
from fractions import *;
from itertools import *; 
import io;
import re;

INF = 987654321987654321987654321;

def readint(delimiter=' ') :
    return map(int, raw_input().split(delimiter));

def readstr(delimiter=' ') :
    return raw_input().split(delimiter);

def readfloat(delimiter=' ') :
    return map(float, raw_input().split(delimiter));

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def bin_search(a, x, left, right) :

    while left<=right :
        mid = (left + right)//2;
        
        if a[mid] == x :
            return mid;
        elif a[mid] < x :
            left = mid + 1; 
        elif a[mid] > x :
            right = mid - 1;
                       
        pass
    
    return -1;
    pass

def printf(format, *args):
    """Format args with the first argument as format string, and write.
    Return the last arg, or format itself if there are no args."""
    sys.stdout.write(str(format) % args)
    pass

if __name__ == '__main__':
    
    tt = readint()[0];
    for tc in xrange(tt) :
        a, b, k = readint();
        count = 0;
        for ii in xrange(0, a) :
            for jj in xrange(0,b) :
                if (ii & jj) < k :
                    #print (ii, jj);
                    count += 1;
                    pass
                pass
            pass
        print "Case #%d: %d"%(tc+1, count);
    pass
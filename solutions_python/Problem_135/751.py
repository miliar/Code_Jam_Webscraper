# -*- coding: utf-8 -*-
"""
Created on Sat Apr 12 12:20:21 2014

@author: rubick
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
    
    tc = readint()[0];
    for ii in xrange(tc) :
        first = readint()[0];
        first_row = None;
        for jj in xrange(4) :
            now = readint();
            if jj+1 == first :
                first_row = now;
                pass
            pass
        
        second = readint()[0];
        second_row = None;
        for jj in xrange(4) :
            now = readint();
            if jj+1 == second :
                second_row = now;
                pass
            pass
        count = 0;        
        ans = -1;
        for xx in first_row :
            if xx in second_row :
                ans = xx;
                count += 1;
        
        if count == 1 :
            ans = str(ans);
            pass
        elif count == 0 :
            ans = 'Volunteer cheated!';
        elif count > 1 :
            ans = 'Bad magician!';
        
        print ("Case #%d: %s")%(ii+1, ans)

    pass
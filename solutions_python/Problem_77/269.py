#!/usr/bin/env python

import sys

def qsort1(list):
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x <pivot])
        greater = qsort1([x for x in list[1:] if x>=pivot])
        return lesser+[pivot] + greater

def solve(N,case):
    case_split = case.split(" ")
    array = [int(x) for x in case_split]
    sort = qsort1(array)

    n = 0
    for i in xrange(0, len(array)):
        if array[i]!=sort[i]:
            n+=1

    #print array, sort, "n=", n

    if n==0:
        return 0
    elif n%2==0:
        return float(n)
    else:
        return n

def parse_args():
    f = open(sys.argv[1]) 
    n = int(f.readline().strip())
   
    for i in xrange(1,n+1):
        N = f.readline().strip()
        case = f.readline().strip()
        print "Case #" + str(i)+ ": %.6f" % solve(N,case)

parse_args()


#!/usr/bin/python

import sys

DEBUG = False

def rotate(s):
    return s[-1]+s[:-1]

def get_rotations(s):
    result=[]
    for i in range(len(s)-1):
        s=rotate(s)
        if s[0]!='0' and s not in result:
            result.append(s)
    return result
 
def count_recycled(A, B):
    result=0
    for n in range(A, B+1):
        rotations=get_rotations(str(n))
        for rotation in rotations:
            if n < int(rotation) <= B:
                if DEBUG:
                    print n, rotation
                result+=1
    return result

sys.stdin.readline()

i=1
for l in sys.stdin:
    A, B = [int(n) for n in l.split()]
    print "Case #%d: %d" % (i, count_recycled(A, B))
    i+=1
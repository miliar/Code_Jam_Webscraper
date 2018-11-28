from __future__ import division
import math


def gcd(a,b):
        if a==0 or b==0: return 0
        while max(a,b)%min(a,b)!=0:
                if b>a: a,b= b,a
                a -=b
        if b>a: a,b= b,a
        return b


f = file("in")
lines = [l for l in f][1:]
case = 0
for line in lines:
        case +=1 
        line = [int(x) for x in line.split(" ")]
        line = line[1:]
        copy = line
        minSecs = min(copy)
        copy = [x-minSecs for x in copy if x != minSecs]
        copy = reduce(gcd, copy)
        if minSecs % copy == 0:
                res = 0
        else:
                res = copy - minSecs % copy
        print "Case #%d: %d" % (case, res)


#TODO: Get rid of L!!!

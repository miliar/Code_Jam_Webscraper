import sys
import math

def calc(l,p,c):
    count = 0
    while l*c < p:
        l *= c
        count += 1
    return count

def calc2(b):
    count = 0
    a = 1
    while not a*2 > b:
        count += 1
        a *= 2
    return count+1


def two():
    t = int(sys.stdin.readline().strip())
    for times in xrange(0,t):
        l,p,c = map(int,sys.stdin.readline().strip().split())
        out = "Case #"+str(times+1)+":"
        one = calc(l,p,c)
        if one == 0:
            two = 0
        else:
            two = calc2(one)
        print out,int(two)

two()


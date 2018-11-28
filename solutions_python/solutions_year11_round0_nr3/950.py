#!/usr/bin/env python

def inp():
    return [eval(x) for x in raw_input().strip().split()]

def solveCase():
    [n] = inp()
    candies = inp()
    xor = lambda x,y:x^y
    if reduce(xor, candies) == 0:
        return "%d" % (sum(candies) - min(candies))
    else:
        return "NO"

def main():
    [ncase] = inp()
    for i in xrange(ncase):
        print "Case #%d: %s" % (i+1, solveCase())

if __name__ == "__main__":
    main()


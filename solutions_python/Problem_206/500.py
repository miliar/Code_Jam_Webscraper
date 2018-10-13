#!/usr/bin/env python2.7
# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

def calc_hour(pos, km, destination):
    return float(destination - pos) / km

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    destination, n = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
    horses = []
    max_hour = -1
    for _ in xrange(n):
        pos, km = [int(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        hour = calc_hour(pos, km, destination)
        if hour > max_hour:
            max_hour = hour
                
    print "Case #{}: {:.6f}".format(i, float(destination) / (max_hour + 0.0000000001))
    # check out .format's specification for more formatting options


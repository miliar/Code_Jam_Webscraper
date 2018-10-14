#!/usr/bin/env python

def is_recycled(n, m):
    pos = len(m) - 1

    while pos > 0:
        if n[pos:] + n[:pos] == m:
            return True
        pos -= 1

    return False


def calculate_recycled(low, high):
    recycled = 0
    current_m = high

    while current_m >= low:
        current_n = current_m - 1
        while current_n >= low:
            if is_recycled(str(current_n), str(current_m)):
                recycled += 1
            current_n -= 1

        current_m -= 1

    return recycled



numtests = None
numcase = 0

f = open('input.txt')
lines = f.readlines()
f.close()

for l in lines:
    if numtests == None:
        numtests = int(l)
    else:
        args = l.split()
        low = int(args[0])
        high = int(args[1])

        numcase += 1
        print "Case #%d: %d" % (numcase, calculate_recycled(low, high))
        

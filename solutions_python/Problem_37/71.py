#!/usr/bin/python

import sys, re
import operator

happy = {}

for b in xrange(2,11):
    happy[1,b] = True

def is_happy(n,b):
    if (n,b) in happy:
        return happy[n,b]
    seen = set([])
    while n not in seen:
        seen.add(n)
        sqrsum = 0
        while n != 0:
            sqrsum += (n%b)**2
            n /= b
        if sqrsum == 1 or (sqrsum,b) in happy:
            return happy[sqrsum,b]
        n = sqrsum
    return False

input_file = open(sys.argv[1])
int_scan = re.compile(r'\d+')
input_data = [[int(x) for x in int_scan.findall(line)] for line in input_file]
input_file.close()

T = input_data[0][0]
input_data = input_data[1:]


for i in xrange(0, T):
    bases = input_data[i]
    n = 2
    while not reduce(operator.__and__, map(lambda b: is_happy(n,b), bases)):
        n += 1
    print "Case #" + str(i+1) + ": " + str(n)
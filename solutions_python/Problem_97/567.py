#!/usr/bin/env python

import sys
import time

# for x <= 2000000
def num_digits(x):
    if   x >= 1000000: return 7
    elif x >=  100000: return 6
    elif x >=   10000: return 5
    elif x >=    1000: return 4
    elif x >=     100: return 3
    elif x >=      10: return 2
    else:              return 1

def cycle_number(x, i):
    divider = 10**i
    a_b = x/divider
    c = x%divider
    return 10**(num_digits(x)-i)*c + a_b

#def recycled_numbers(s, x):
#    s.clear()
#    for i in xrange(num_digits(x)):
#        s.add(cycle_number(x, i+1))

def recycled_numbers(s, x):
    s.clear()
    divider = 10
    digits = num_digits(x)
    factor = 10**(digits-1)
    for i in xrange(digits):
        a_b = x/divider
        c = x%divider
        s.add(factor*c + a_b)
        divider *= 10
        factor /= 10

# ----- main -----

infile = open(sys.argv[1])
outfile = open(sys.argv[2], "w")

numcases = int(infile.readline())

sys.stdout.write("time=%f\n"%time.time())

s = set()

for case in xrange(numcases):
    l = infile.readline().split()
    A = int(l[0])
    B = int(l[1])
    result = 0
    i = A
    while i <= B:
        recycled_numbers(s, i)
        for candidate in s:
            #print "A=%d, B=%d, i=%d, candidate=%d"%(A,B,i,candidate)
            if candidate > i and candidate >= A and candidate <= B:
                result += 1

        i += 1
    outfile.write("Case #%d: %d\n"%(case+1, result))
    sys.stdout.write("Case #%d: %d (%f)\n"%(case+1, result, time.time()))

outfile.close()
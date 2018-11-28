# Has been a great while since I coded...Here Goes
# Snapper
# Usage pretty simple: Q1.py <inputfile>
# requires a EOF to terminate


#Read Input - Absolutely 0 input checks

import fileinput

infile = fileinput.input()

p = infile.readline()

N = long(p)

n = 0

while n < N:
    n += 1
    params = infile.readline()
    S,C = [long(p) for p in params.split()]
    s = pow(2,S) - 1
    if (s & C) >= s:
        print "Case #%d: ON" % n
    else:
        print "Case #%d: OFF" % n

infile.close()


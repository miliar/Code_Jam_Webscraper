#!/usr/bin/python

import sys

from math import ceil

def gcd(a, b):
    """
    Greatest common denominator.
    Numerator a and denominator b.
    a, b to be positive int values or zero.
    Originally posted by Rasheed"""
    # Thanks to http://www.python-forum.org/pythonforum/viewtopic.php?f=2&t=7262#p34099

    if a<b:
        (a,b) = (b,a)
    
    while b != 0:
        a, b = b, a % b
    return a 


def calc_y(N):

    # Sort so the biggest is the last one
    N.sort()
    g = None
    for i in xrange(len(N)-1):
        v = N[-1] - N[i]
        # GCD is associative...
        if g is None:
            g = v
        else:
            g = gcd(v,g)
    # Y is the complement to the gcd of the biggest value
    y = g * int(ceil(float(N[-1])/g))-N[-1]
    return y



def main(nameIn, nameOut):
    """Read form the input and write thr Case #:"""

    
    fI = open(nameIn, 'r')
    fO = open(nameOut, 'w')

    # First line is the number of cases
    l = fI.readline()
    Nl = int(l[0:-1])

    i=0    
    for line in fI:
        line = line.strip() # This will remove the \n also
        if len(line)==0:
            continue
        i += 1
        if i>Nl:
            break
        Val = [ int(x) for x in line.split() ]
        y = calc_y(Val[1:])
        fO.write("Case #" + str(i) + ": " + str(y) + "\n")
    fI.close()
    fO.close()


if __name__ == "__main__":    
    if len(sys.argv)<3:
        print("Usage: " + sys.argv[0] + " <file_in> <file_out>")
        exit(0)

    main(sys.argv[1], sys.argv[2])

    

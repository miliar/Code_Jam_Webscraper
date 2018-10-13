#!/usr/bin/env python

from sys import argv, stderr

def main(filename):
    
    file = open(filename)

    T = int(file.readline())
    
    count = 0

    for line in file:
        N, K = line.strip().split()

        count += 1

        N = int(N)
        K = int(K)

        value = 0
        
        for i in xrange(0,N):
            value += 2**i
        
        result = K

        result &= (1L << N) - 1

        if result == value:
            onoff = "ON"
        else:
            onoff = "OFF"

        print "Case #%u: %s" % (count, onoff)

if __name__ == "__main__":
    main(argv[1])

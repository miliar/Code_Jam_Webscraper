#/!usr/bin/python

import sys

#import psyco
#psyco.full()

def check(n, k):
    return (k + 1) % (2**n) == 0
   
def main():
    inputfile = open(sys.argv[1])
    t = int(inputfile.readline().strip())
    outputfile = open(sys.argv[1] + ".out", "w")
    for i in xrange(t):
        n, k = [int(x) for x in inputfile.readline().strip().split()]
        result = check(n, k)
        outputfile.write("Case #%d: %s\n" % (i+1, "ON" if result else "OFF"))

if __name__ == "__main__":
    main()

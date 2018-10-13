#!/usr/bin/python

import sys

def main():
    inputfile = open(sys.argv[1])
    outputfile = open(sys.argv[1] + ".out", "w")
    t = int(inputfile.readline().strip())
    for i in xrange(t):
        R, k, N = [int(x) for x in inputfile.readline().strip().split()]
        groups = [int(x) for x in inputfile.readline().strip().split()]
        count = 0
        for j in xrange(R):
            kc = k
            coaster = []
            while groups and groups[0] <= kc:
                first = groups.pop(0)
                kc -= first
                count += first
                coaster.append(first)
            groups += coaster
        outputfile.write("Case #%d: %d\n" % (i+1, count))

if __name__ == "__main__":
    main()

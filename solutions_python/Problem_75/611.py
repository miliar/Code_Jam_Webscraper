#!/usr/bin/python

import sys

import psyco
psyco.full()

def main():
    # Read in
    infile = open(sys.argv[1])
    numtests = int(infile.readline())
    for i in range(numtests):
        line = infile.readline().strip().split()
        numcombiners = int(line[0])
        combiners = line[1:1+numcombiners]
        combiners = dict([(x[:2], x[2]) for x in combiners] + [(x[:2][::-1], x[2]) for x in combiners])
        line = line[numcombiners+1:]
        numopposers = int(line[0])
        opposers = line[1:1+numopposers]
        opposers = dict([(x[0],x[1]) for x in opposers] + [(x[1],x[0]) for x in opposers])
        line = line[numopposers+1:]
        input = list(line[1])
        assert len(line)==2, line

        output = []
        for c in input:
            output.append(c)
            final_pair = "".join(output[-2:])
            if final_pair in combiners:
                output[-2:] = [combiners[final_pair]]
            elif c in opposers and opposers[c] in output:
                output = []
        print "Case #%d: [%s]" % (i+1, ", ".join(output))

if __name__ == "__main__":
    main()

#!/usr/bin/python

# Drew Gassaway
# GCJ 2014 Qualification A

import sys

BADMAG = "Bad magician!"
CHEATR = "Volunteer cheated!"

def trick (infile, outfile):

    with open(infile, "r") as fp:

        out = open(outfile, "w")
        numcases = int(fp.readline().strip())

        for casenum in range(numcases):

            a1 = int(fp.readline().strip())

            set1 =set()
            for row in range(4):
                line = fp.readline().strip()
                if (row + 1) != a1:
                    continue
                set1 = set(line.split(' '))

            a2 = int(fp.readline().strip())

            set2 = set()
            for row in range(4):
                line = fp.readline().strip()
                if (row + 1) != a2:
                    continue
                set2 = set(line.split(' '))

            overlap = set1 & set2

            # debug
            #print "set1: " + str(set1)
            #print "set2: " + str(set2)
            #print "1&2 : " + str(overlap)

            if len(overlap) < 1:
                result = CHEATR
            elif len(overlap) == 1:
                result = overlap.pop()
            else:
                result = BADMAG

            out.write("Case #" + str(casenum + 1) + ": " + result + '\n')

        out.close()


### Main

if len(sys.argv) != 3:
    print "Usage: " + sys.argv[0] + " <input_file> <output_file>"
    exit(1)

trick(sys.argv[1], sys.argv[2])


#!/usr/bin/env python

from sys import argv

FILENAME = argv[1]
INFILE = FILENAME + ".in"
OUTFILE = FILENAME + ".out"

fin = open(INFILE, "r")
print "Input: ", INFILE
fout = open(OUTFILE, "w")
print "Output: ", OUTFILE

print

T = int(fin.readline().strip())
for i in range(T):
    root = {}
    [N, M] = map(int, fin.readline().strip().split(' '))

    for j in range(N):
        here = root
        for name in fin.readline().strip()[1:].split('/'):
            if not here.has_key(name):
                here[name] = {}
            here = here[name]

    count = 0
    for j in range(M):
        here = root
        for name in fin.readline().strip()[1:].split('/'):
            if not here.has_key(name):
                here[name] = {}
                count += 1
            here = here[name]

    fout.write("Case #" + str(i+1) + ": " + str(count) + "\n")
    print "Case #" + str(i+1) + ": " + str(count)

fin.close()
fout.close()

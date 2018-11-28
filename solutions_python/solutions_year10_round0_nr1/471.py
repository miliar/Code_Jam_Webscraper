# snapper question

from sys import argv
from re import match

print argv[1]

file = open(argv[1])

line1 = file.readline()
testc = int(line1)

outfile = open(argv[1] + ".out", "w")

print "testc is ", testc

for testnum in range(1, testc+1):
    line = file.readline().split(" ")
    N = int(line[0])
    K = int(line[1]) 

    if (K % 2**N) + 1 == 2**N:
        state = "ON"
    else:
        state = "OFF"

    print >>outfile, "Case #%d: %s" % (testnum, state)


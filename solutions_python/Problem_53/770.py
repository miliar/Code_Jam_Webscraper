#usr/bin/env python
import sys
numcases = int(sys.stdin.readline())

for case in range(1,numcases + 1):
    data = sys.stdin.readline().split()
    if int(data[1]) & ((2 ** (int(data[0])) - 1)) == ((2 ** (int(data[0])) - 1)):
        output = "ON"
    else:
        output = "OFF"
    print "Case #%d: %s" % (case, output)

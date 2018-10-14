#! /usr/bin/python

import sys

if len(sys.argv) < 2:
    print("Usage: ./p1.py <input file>")
    sys.exit(1)

try:
    fin = open(sys.argv[1])
except IOError:
    print("Input file not found")
    sys.exit(1)

data = fin.readlines()
fin.close()
ind = 1
num = int(data[0].strip())

for i in xrange(num):
    rownum = int(data[ind].strip())
    row1 = data[ind+rownum].strip().split()
    ind += 5
    rownum2 = int(data[ind].strip())
    row2 = data[ind+rownum2].strip().split()
    ind += 5
    result = 0
    resultnum = 0
    for val in row1:
        if val in row2:
            result += 1
            resultnum = val
    if result == 0:
        print "Case #%d: Volunteer cheated!"%(i+1)
    elif result == 1:
        print "Case #%d: %s"%(i+1, resultnum)
    else:
        print "Case #%d: Bad magician!"%(i+1)

sys.exit(0)

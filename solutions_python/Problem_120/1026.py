import math

def getRingCount(radius, paints):
    a = 2
    b = 2*radius - 1
    c = paints      # negative
    n = math.sqrt(b*b + 4*a*c) - b
    n = n / 4
    n = math.floor(n)
    if (2*n*n + n*(2*radius-1)) <= paints:
        return n
    else:
        return n - 1


import sys
#import pdb

fileNamePrefix = sys.argv[1]
fileNameIn = fileNamePrefix + ".in"
fileNameOut = fileNamePrefix + ".out"

fileIn = open(fileNameIn, 'r')
lines = fileIn.readlines()

testcnt = int(lines[0])
idx = 1

fileOut = open(fileNameOut, 'w')

#pdb.set_trace()

for test in range(testcnt):
    line = lines[idx].split(' ')
    idx += 1

    r = int(line[0])
    t = int(line[1])
    res = getRingCount(r, t)
    fileOut.write("Case #{0}: {1}\n".format(test + 1, res))

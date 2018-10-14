# Google Code Jam 2014 - Cookie Clicker Alpha
# Guy Weizman

import math # Standard python math library
import sys

__author__ = 'Guy Weizman'


# Calculates the time for n farms
def getTime(n, C, F, X):
    f = 2
    t = 0
    if (n > 0):
        for i in range(n):
            t += (C/(f))
            f += F
    return t + X/f

if (len(sys.argv) != 2):
    print 'Syntax: python cookie.py FILE_PATH [Without .in]'
    exit()

file = sys.argv[1]

readFile = open(file + '.in', 'r')
writeFile = open(file + '.out', 'w')

testCases = int(readFile.readline())

for i in range(testCases):
    line = readFile.readline().split()
    C = float(line[0])
    F = float(line[1])
    X = float(line[2])
    # Calculated n by hand as the highest number of farms that provides time improvement
    n = int(math.ceil(((X/C - 1) - 2/F)))
    writeFile.write("Case #" + str(i + 1) + ": " + format(getTime(n, C, F, X),'.7f') + "\n")
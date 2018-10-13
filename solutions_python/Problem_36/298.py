#!/usr/bin/env python

import sys
import string
import re

checker = re.compile(r".*w.*e.*l.*c.*o.*m.*e.* .*t.*o.* .*c.*o.*d.*e.* .*j.*a.*m.*")

theString = "welcome to code jam"

def findStrings(aString, strLen, strIdx = 0, findIdx = 0):
    global theString
    total = 0
    for i in range(strIdx, strLen):
        if aString[i] == theString[findIdx]:
            if findIdx == 18:
                total += 1
            else:
                total += findStrings(aString, strLen, i + 1, findIdx + 1)
    return total

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: %s <dataset_name>" % sys.argv[0]
        sys.exit(1)
    
    inFile = open(sys.argv[1] + ".in", "r")
    lines = map(lambda x: x[:-1], inFile.readlines())
    inFile.close()
    
    N = int(lines[0])
    del lines[0]
    
    cases = []
    
    for line in lines:
        if checker.match(line):
            cases.append(findStrings(line, len(line)))
        else:
            cases.append(0)
    
    outFile = open(sys.argv[1] + ".out", "w")
    for i in range(len(cases) - 1):
        outFile.write("Case #%d: %04d\n" % (i + 1, cases[i]))
    outFile.write("Case #%d: %04d" % (len(cases) - 1 + 1, cases[len(cases) - 1]))
    outFile.close()
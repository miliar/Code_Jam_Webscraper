#!/usr/bin/env python

import sys
import string
import re

splitter = re.compile(r"\(([a-z]+)\)|([a-z]+)")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: %s <dataset_name>" % sys.argv[0]
        sys.exit(1)
    
    inFile = open(sys.argv[1] + ".in", "r")
    lines = map(lambda x: x[:-1], inFile.readlines())
    inFile.close()
    
    header = lines[0]
    del lines[0]
    (L, D, N) = map(int, header.split(" "))
    
    words = set(lines[:D])
    patterns = lines[D:D+N]
    
    patres = []
    
    cases = []
    for pattern in patterns:
        patst = string.replace(pattern, '(', '[')
        patst = string.replace(patst, ')', ']')
        patres.append(re.compile(patst))
        cases.append(0)
    
    for word in words:
        for i in range(len(patres)):
            if patres[i].match(word):
                cases[i] += 1
    
    outFile = open(sys.argv[1] + ".out", "w")
    for i in range(len(cases) - 1):
        outFile.write("Case #%d: %d\n" % (i + 1, cases[i]))
    outFile.write("Case #%d: %d" % (len(cases) - 1 + 1, cases[len(cases) - 1]))
    outFile.close()
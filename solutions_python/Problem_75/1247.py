#!/usr/bin/env python

import sys
import re

fh = open(sys.argv[1])

T = int(fh.readline())

def check_combined(elements, letters):
    for i in range(len(letters)):
        element1 = letters[i][:2][0]
        element2 = letters[i][:2][1]
        non_element = letters[0][-1]
        regexp = '%s%s|%s%s' % (element1, element2, element2, element1)
        if re.search(regexp, ''.join(elements[-2:])):
            elements[-2:] = non_element
            return True
        else:
            return False

def check_opposed(elements, opposed):
    if len(opposed) > 0:
        for i in range(len(opposed)):
            element1, element2 = opposed[i]
            if element1 in elements and element2 in elements:
                elements[:] = []

for i in range(T):
    result = []
    combined = []
    opposed = []
    line = fh.readline().split()
    C = int(line[0])
    D = int(line[C+1])
    if C > 0:
        combined = line[1:C+1]
    if D > 0:
        opposed = line[C+2:C+D+2]
    word = line[-1]
    for j in range(len(word)):
        result.append(word[j])
        if len(result) >= 2:
            if len(combined) > 0 and check_combined(result,combined):
                continue
            else:
                check_opposed(result, opposed)
        
    print "Case #%s: [%s]" % (i+1, ', '.join(result))

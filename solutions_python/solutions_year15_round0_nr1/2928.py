#!/usr/bin/python

import sys
from file_handler import readfile, writesoluce

def resolveCase(case):
    cnt = 0
    stand = 0

    print case
    for i in range(len(case)):
        if i == 0:
            stand = case[i]
        else:
            if stand < i:
                people = (i - stand)
                cnt   += people
                stand += people
            stand += case[i]
    return cnt

def resolveCases(cases):
    solucs = list()
    for case in cases:
        solucs.append(resolveCase(case))
    return solucs

if __name__ == "__main__":
    cases = readfile(sys.argv[1])
    solucs = resolveCases(cases)
    writesoluce('output.txt', solucs)

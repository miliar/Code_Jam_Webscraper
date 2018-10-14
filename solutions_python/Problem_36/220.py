#!/usr/bin/env python
import sys

def line():
    return sys.stdin.readline()[:-1]

def suffixes(s):
    return [s[i:] for i in range(len(s))]

if __name__ == "__main__":
    N = eval(line())
    # We set up some general stuff
    searchString = "welcome to code jam"
    keySuffixes = suffixes(searchString)
    usefulLetters = set(searchString)
#    print usefulLetters
#     suffixesStartingWith = dict()
#     for c in usefulLetters:
#         suffixesStartingWith[c] = []
#         for suffix in keySuffixes:
#             if suffix[0] == c:
#                 suffixesStartingWith[c].append(suffix)
#     print suffixesStartingWith
#    print keySuffixes
    
    for caseNumber in range(1,N+1):
        caseString = line()
        numberOfWays = dict()
        for i in range(len(caseString)+1):
            numberOfWays[i] = dict()
            for keySuffix in keySuffixes:
                numberOfWays[i][keySuffix] = 0
            numberOfWays[i][""] = 1
        for i in range(len(caseString)-1,-1,-1):
            for suffix in keySuffixes:
                if suffix[0] == caseString[i]:
                    numberOfWays[i][suffix] = numberOfWays[i][suffix] + numberOfWays[i+1][suffix[1:]]
                    pass
                numberOfWays[i][suffix] = numberOfWays[i][suffix] + numberOfWays[i+1][suffix]
        
        print "Case #" + str(caseNumber) + ": " + "%04d" % (numberOfWays[0][searchString] % 10000)

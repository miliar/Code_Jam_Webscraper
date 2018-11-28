#!/usr/bin/python

import sys

inputfile = open(sys.argv[1], 'r').read().split('\n')
outputfile = open("./output.large.1", 'w')

numcases = int(inputfile[0])
currcase = 0
totallines = 1

while currcase < numcases:
        enginedict = {}
        switches = 0
        numengines = inputfile[totallines]
        totallines += 1
        for engine in inputfile[totallines:totallines + int(numengines)]:
                enginedict[engine] = 0
        totallines += len(enginedict.keys())
        numqueries = int(inputfile[totallines])
        totallines += 1
        queriesleft = numqueries
        while queriesleft > 0:
                enginedict[inputfile[totallines + queriesleft - 1]] += 1
                untouched = 0
                for engine in enginedict.keys():
                        if not enginedict[engine]:
                                untouched = 1
                if not untouched:
                        switches += 1
                        queriesleft += 1
                        for engine in enginedict.keys():
                                enginedict[engine] = 0
                queriesleft -= 1
        totallines += int(numqueries)
        currcase += 1
        outputfile.write("Case #" + str(currcase) + ": " + str(switches) + '\n')
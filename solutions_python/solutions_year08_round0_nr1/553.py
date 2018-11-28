#!/bin/python
import sys

#My Solution: Find the furthest engine, switch to it, and drop all queries
#occuring before it. Repeat
def countSwitches(engines, queries):
    #Switches = 0 as the cost of the first switch is nothing
    switches = 0
    #Whilst their remain queries we have yet to see
    while len(queries) > 0:
        distance = 0
        try:
            #Find the engine furthest away
            for engine in engines:
                if (queries.index(engine) > distance):
                    distance = queries.index(engine)
            switches += 1
        #ValueError raised by index(engine) when engine not found
        except ValueError:
            #If and engine isn't found, we switch to it and we're done.
            queries = []

        #Now remove the seen queries
        queries = queries[distance:]
        
    return switches

#Open the file, deal with any errors
if len(sys.argv) < 2:
    print 'Please Specify An Input File!'
    exit()

inputFile = sys.argv[1]
try:
    inputFile = open(inputFile, 'r')
except IOError:
    print 'Input File Invalid'
    exit()

#This code relies heavily on the constraints given, and does not respond
#well to errors

#Read in the file into a nice format
uglyLines = inputFile.readlines()
fileLines = []
for line in uglyLines:
    fileLines.append(line.strip('\n'))

#The first line gives us the number of test cases
testCases = int(fileLines[0])

#Now we know the number, we drop the first line off
fileLines = fileLines[1:]

#Now go through each test
for i in range(testCases):
    #The first line gives us the engines
    numEngines = int(fileLines[0])
    #Then we extract them
    curEngines = fileLines[1:(numEngines + 1)]
    fileLines = fileLines[(numEngines + 1):]
    
    #The first line now gives us the queries
    numQueries = int(fileLines[0])
    
    #Then we extract them
    curQueries = fileLines[1:(numQueries + 1)]
    fileLines = fileLines[(numQueries + 1):]
    
    #Now we print the number of switches needed
    if numQueries > 0:
        print 'Case #' + str(i+1) + ': ' + str(countSwitches(curEngines, curQueries))
    else:
        print 'Case #' + str(i+1) + ': 0'

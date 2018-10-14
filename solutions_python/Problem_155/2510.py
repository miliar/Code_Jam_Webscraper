#!/bin/python

testFile = open("/tmp/input.txt")
totalCases = int(testFile.readline())

for case in range(1, totalCases + 1):
    line       = testFile.readline()
    tokens     = line.split()
    maxShyness = int(tokens[0])
    audience   = tokens[1]
    
    if (maxShyness == 0 or (not '0' in audience)):
        print "Case #{}: {}".format(case, 0)
        continue

    easilyImpressed = int(audience[0])

    if (easilyImpressed == 0):
        friends      = 1
        alreadyThere = 0
    else:
        friends      = 0
        alreadyThere = easilyImpressed

    for i in range(1, maxShyness + 1):
        currentAudience = int(audience[i])
        
        if (currentAudience != 0):
            total = friends + alreadyThere

            if (total < i):
                friends += (i - total)
                
            alreadyThere += currentAudience

    print "Case #{}: {}".format(case, friends)
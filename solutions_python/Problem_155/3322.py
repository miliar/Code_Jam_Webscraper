#!/usr/bin/env python3.4
"""
Google Code Jam 2015 Qualification Round
Problem A: Standing Ovation

Find number of invites needed to create a standing ovation given shyness levels

@author Jeffrey Owens
"""

def findTotalInvites(audienceString):
    totalClapping = 0
    totalInvites = 0
    # eg. audience=409 means 4 members at shyLevel 0, 9 members as shyLevel 2.
    for shyLevel, numMembers in enumerate(audienceString, start=0):
        if int(numMembers) > 0 and shyLevel > totalClapping:
            # Invite people until this shyness level starts clapping.
            invites = shyLevel - totalClapping
            totalInvites += invites
            totalClapping += invites
            # Note: we could record the shyness level of the invites, but that level is arbitrary
        totalClapping += int(numMembers)

    return totalInvites

def testFindTotalInvites():
    # NOTE: test(s) should probably be more complex than this.
    audience = "110011" # could do an iterable array of audience tests
    result = findTotalInvites(audience)
    # Expected result: 2. shyLevel 4 needs 2 invites to trigger.
    print("Test case: audience = " + audience + " result = " + str(result))
    

inputFile = 'A-large.in'
outputFile = 'A-large.out'

dataIn = open(inputFile, 'r')

# Note: because of Python iterables, numCases is thrown out. Left for explicitness.
numCases = int(dataIn.readline())
fullResults = ''

for case, dataLine in enumerate(dataIn, start=1):
    maxShyLevel, audience = dataLine.rstrip().split(' ')
    # Note: maxShyLevel+1 defines length of audience string, not very useful here.

    totalInvites = findTotalInvites(audience)

    resultOut = "Case #" + str(case) + ": " + str(totalInvites)
    print(resultOut)
    fullResults += resultOut + "\n"

dataIn.close()

dataOut = open(outputFile, 'w')
dataOut.write(fullResults)
dataOut.close()

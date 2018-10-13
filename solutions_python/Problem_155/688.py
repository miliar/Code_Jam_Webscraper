# CodeJam 2015 Problem A
# Nicholas Sharp - nsharp33@gmail.com

import fileinput

nCases = int(raw_input())

for iCase in range(nCases):

    s = raw_input().split(" ")
    maxShy = int(s[0])
    countStr = s[1]

    nStanding = 0
    added = 0
    for shyness in range(0,maxShy+1):

        #print("Standing  = " + str(nStanding) + " shyness = " + str(shyness))

        numThis = int(countStr[shyness])

        if(nStanding < shyness):
            added += shyness - nStanding
            nStanding = shyness

        nStanding += numThis

    print("Case #%d: %d"%(iCase+1, added))

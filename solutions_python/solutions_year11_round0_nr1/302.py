
import string, os, time, sys


def HandleCase(f, caseIndex):
    caseline = f.readline().rstrip("\r\n")
    splitline = caseline.split(" ")
    numOperations = int(splitline[0])
    OPushes = []
    BPushes = []
    OsTurn = []
    for i in range(0,numOperations):
        if (splitline[i*2+1] == "O"):
            OPushes.append(int(splitline[i*2+2]))
            OsTurn.append(True)
        else:
            BPushes.append(int(splitline[i*2+2]))
            OsTurn.append(False)

    ODistances = []
    if (len(OPushes)>0):
        ODistances.append(OPushes[0]-1)
    for i in range(0,len(OPushes)-1):
        ODistances.append(abs(OPushes[i]-OPushes[i+1]))

    BDistances = []
    if (len(BPushes)>0):
        BDistances.append(BPushes[0]-1)
    for i in range(0,len(BPushes)-1):
        BDistances.append(abs(BPushes[i]-BPushes[i+1]))

    result = 0
    while (len(OsTurn) > 0):
        osTurn = OsTurn.pop(0)
        if osTurn:
            if (len(BDistances) > 0):
                if (BDistances[0] < ODistances[0]+1):
                    BDistances[0] = 0
                else:
                    BDistances[0] = BDistances[0] - (ODistances[0]+1)
            result = result + ODistances.pop(0) + 1

        else:
            if (len(ODistances) > 0):
                if (ODistances[0] < BDistances[0]+1):
                    ODistances[0] = 0
                else:
                    ODistances[0] = ODistances[0] - (BDistances[0]+1)
            result = result + BDistances.pop(0) + 1
            
    header = "Case #%(count)d:" % {"count":caseIndex}
    print header,
    print result
    
    

inputFile = sys.argv[1]
f = open(inputFile, "r")
numCases = int(f.readline())
for i in range(0, numCases):
    HandleCase(f, i+1)


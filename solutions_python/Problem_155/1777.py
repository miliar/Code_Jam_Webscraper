#code jam #1

import sys

input = open(sys.argv[1])

numOfTests = int(input.readline())

def solve(rawStr):
    maxStr, dataStr = rawStr.strip().split(" ")
    maxShy = int(maxStr)

    shylist = [int(x) for x in dataStr]
    additional = 0
    standingpeople = 0

    shyness = 0
    while shyness < len(shylist):
        numOfCurShyness = shylist[shyness]
        extrapeople = 0 if shyness <= standingpeople else (shyness - standingpeople)
        additional += extrapeople
        standingpeople += extrapeople + shylist[shyness]
        shyness += 1
    return str(additional)

counter = 1
for row in input:
    print "Case #" + str(counter) + ": " + solve(row)
    counter += 1

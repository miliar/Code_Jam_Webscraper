import os
import math

# Create Output file
f = open('dataOut.txt', "w")
f.close()

# Read Input file
f = open('A-small-attempt1.in', "rb")
numOfTestCases = f.readline()
numOfTestCases = int(numOfTestCases)

# Loop through cases
for i in range(0,numOfTestCases):
    NDG = f.readline()
    NDG = NDG.split()
    N = int(NDG[0])
    PD = float(NDG[1])
    PG = int(NDG[2])
    isPossible = False
    PD = PD / 100

    for j in range(1,N+1):
        ans = PD * j
        if ((ans % 1 == 0) & (PG != 100)):
            isPossible = True
            break
    if ((PG == 100) & (PD == 1)):
        isPossible = True
    if ((PG == 100) & (PD < 1)):
        isPossible = False
    if ((PG == 0) & (PD > 0)):
        isPossible = False

    g = open('dataOut.txt', "a")
    caseNum = i+1
    if isPossible:
        g.write("Case #" + repr(caseNum) + ": Possible" + "\n")
    else:
        g.write("Case #" + repr(caseNum) + ": Broken" + "\n")
    g.close()
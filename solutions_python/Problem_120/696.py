#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Wesley D
#
# Created:     27/04/2013
# Copyright:   (c) Wesley D 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

Input = open(raw_input("Enter Input Path:"))
InputList = []
for line in Input:
    InputList.append(line[:-1])

Input.close()
InputList.pop(0)
OutputList = []
caseNum = 0
for case in InputList:
    caseNum += 1
    r = int(case.split()[0])
    t = int(case.split()[1])
    rings = 0
    while t > 0:
        if (((r+1)**2) - (r**2)) > t:
            break
        else:
            t -= ((r+1)**2) - (r**2)
            r+=2
            rings += 1
    OutputList.append("Case #" + str(caseNum) + ": " + str(rings))

Output = open(raw_input("Enter Output Path:"), "wb")
for caseline in OutputList:
    Output.write(caseline + "\r\n")

Output.close()
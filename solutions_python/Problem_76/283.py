instructionFile = open("instructions.txt", "r").readlines()
numCases = 0
caseNo = 1
bagSize = 0
for line in instructionFile:
    smallest = 0
    total = 0
    xtotal = 0
    for word in line.split():
        if numCases == 0:
            numCases = int(word)
        elif bagSize == 0:
            bagSize = int(word)
        else:
            value = int(word)
            if smallest == 0:
                smallest = value
            else:
                smallest = min(smallest, value)
            total = total + value
            xtotal = xtotal ^ value

    if total != 0:
        if xtotal != 0:
            print("Case #", caseNo, ": NO", sep="")
        else:
            print("Case #", caseNo, ": ", total - smallest, sep="")
        bagSize = 0
        caseNo = caseNo + 1

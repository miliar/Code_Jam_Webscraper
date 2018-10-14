fIn = open("input.in","r")
fOut = open("output.txt","w")
numberOfCasesStr = fIn.readline()
numberOfCasesSplit = numberOfCasesStr.split()
numberOfCases = int(numberOfCasesSplit[0])
for i in range(numberOfCases):
    numberOfWeightsStr = fIn.readline()
    numberOfWeightsSplit = numberOfWeightsStr.split()
    numberOfWeights = int(numberOfWeightsSplit[0])
    nList = []
    kList = []
    nCountNormal = 0
    nCountDeceit = 0
    naomiWeightsStr = fIn.readline()
    naomiWeightsSplit = naomiWeightsStr.split()
    for item in naomiWeightsSplit:
        nList.append(float(item))
    kenWeightsStr = fIn.readline()
    kenWeightsSplit = kenWeightsStr.split()
    for item in kenWeightsSplit:
        kList.append(float(item))
    nListCopy = nList[:]
    kListCopy = kList[:]
    nListCopy.sort()
    kListCopy.sort()

    for item1 in nListCopy:
        differences = {}
        count = 0
        for item2 in kListCopy:
            difference = item2 - item1
            if difference > 0:
                differences[count] = difference
            count = count + 1
        if len(differences) != 0:
            minimum = min(differences.values())
            pos = list(differences.keys())[list(differences.values()).index(minimum)]
            del kListCopy[pos]
    nCountNormal = len(kListCopy)

    nListCopy = nList[:]
    kListCopy = kList[:]
    nListCopy.sort()
    kListCopy.sort()

    while len(nListCopy) != 0:
        item3 = nListCopy[0]
        item4 = kListCopy[0]
        if item3 < item4:
           nListCopy.remove(item3)
           del kListCopy[-1]
        else:
           nListCopy.remove(item3)
           kListCopy.remove(item4)
           nCountDeceit = nCountDeceit + 1

    line = "Case #{}: ".format(i+1) + str(nCountDeceit) + " " + str(nCountNormal)
    fOut.write(line)
    fOut.write("\n")
fIn.close()
fOut.close()



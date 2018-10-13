import sys

name = "C-small-1-attempt0"
path = ""
sys.stdin = open(path+name+".in")
sys.stdout = open(path+name+".out", 'w')
testCases = int(input())



def getEmptyRange(local_ocupedStalls):
    myrange = []
    final = local_ocupedStalls[len(local_ocupedStalls) - 1]
    for index in range(0, len(local_ocupedStalls), 1):
        if local_ocupedStalls[index] != final:
            init = local_ocupedStalls[index] + 1
            if index+1 >= len(local_ocupedStalls):
                fin = int(len(local_ocupedStalls))
            else:
                fin = local_ocupedStalls[index+1] - 1
            myrange.append([init, fin])
    return myrange


def getMidleBathrooms(index_init, index_fin):
    batrooms = []
    auxN = index_fin - index_init + 1
    if auxN % 2 == 0: #par
        middle_a = int(index_init + (auxN / 2 - 1))
        middle_b = int(index_init + (auxN / 2))
        batrooms.append(middle_a)
        batrooms.append(middle_b)
    else: #impar
        middle_a = int(index_init + (auxN/2 - .5))
        batrooms.append(middle_a)
    return batrooms

def calculateLR(i, ocupadosBathrooms): #Naux: how many empty stalls i:index of the stall
    res ={"Ls":0, "Rs":0}
    auxOcupedStalls = list(ocupadosBathrooms)
    auxOcupedStalls.append(i)
    auxOcupedStalls.sort()
    for a in range(auxOcupedStalls[auxOcupedStalls.index(i) - 1], i-1):
        res["Ls"] += 1
    if auxOcupedStalls.index(i) + 1 < len(auxOcupedStalls):
        for a in range(i, auxOcupedStalls[auxOcupedStalls.index(i) + 1]-1):
            res["Rs"] +=1
    else:
        for a in range(i, auxOcupedStalls[auxOcupedStalls.index(i)]-1):
            res["Rs"] += 1
    return res

for testCase in range(1, testCases+1):
    rowInput = input()
    ocupedStalls = list([0])
    listRowInput = rowInput.split(' ')
    N = int(listRowInput[0])
    K = int(listRowInput[1])
    ocupedStalls.append(N+1)
    LR_max = 0
    LR_min = 0
    while K > 0:
        myRanges = getEmptyRange(ocupedStalls)
        availableBatrooms = []
        for iRanges in myRanges:
            availableBatrooms.append(iRanges[1] - iRanges[0] + 1)
        interestRange = myRanges[availableBatrooms.index(max(availableBatrooms))]
        #for iRanges in myRanges:
        midleBathrooms = getMidleBathrooms(interestRange[0], interestRange[1])
        #if len(midleBathrooms) == 2: #si son pares
        bath_LR_left = calculateLR(midleBathrooms[0], ocupedStalls)
        LR_max = max([bath_LR_left["Ls"], bath_LR_left["Rs"]])
        LR_min = min([bath_LR_left["Ls"], bath_LR_left["Rs"]])
        ocupedStalls.append(midleBathrooms[0])
        ocupedStalls.sort()
        K -= 1
    print("Case #{}: {} {}".format(testCase, LR_max, LR_min))
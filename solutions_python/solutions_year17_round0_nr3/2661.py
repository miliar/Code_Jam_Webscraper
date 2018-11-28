

def calcLs(stallList, currDex):
    for num in range(1, len(stallList)):
        if stallList[num] == currDex:
            return stallList[num] - stallList[num - 1] - 1

def calcRs(stallList, currDex):
    for num in range(len(stallList) - 1, 0, -1):
        if stallList[num] == currDex:
            return stallList[num + 1] - stallList[num] - 1

def findGap(stallList):
    maxGap = - 1
    start, end = 0, 0
    for i in range(len(stallList) - 1):
        if stallList[i + 1] - stallList[i] > maxGap:
            start = stallList[i]
            end = stallList[i + 1]
            maxGap = end - start
    return start, end

def play(listSize, numPeople):
    # if numPeople == 1: return listSize // 2, listSize // 2 - 1
    # elif numPeople > (listSize // 2 + 1): return 0, 0

    stallList = [0, listSize + 1]
    start, end = 0, listSize + 1
    for num in range(numPeople - 1):
        stallList.append((end - start) // 2 + start)
        stallList = sorted(stallList)
        start, end = findGap(stallList)

    lastPersonDex = (end - start) // 2 + start
    stallList.append(lastPersonDex)
    stallList = sorted(stallList)

    Ls = calcLs(stallList, lastPersonDex)
    Rs = calcRs(stallList, lastPersonDex)

    return max(Ls, Rs), min(Ls, Rs)



if __name__ == '__main__':
    inputName = "smallBathroomOne.txt"
    outputName = "outputSmallBathroomOne(2).txt"
    f = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/" + inputName,'r')
    w = open("/Users/benhubsch/Dropbox/Side Projects/Google Code Jam/" + outputName,'w')
    case = 0
    for line in f:
        if case != 0:
            arg1, arg2 = int(line.strip().split()[0]), int(line.strip().split()[1])
            maxOut, minOut = play(arg1, arg2)
            w.write("Case #" + str(case) + ": " + str(maxOut) + " "+ str(minOut) + "\n")
        case += 1
    f.close()
    w.close()
    # print(play(3,1))



# def initialize(stalls):
#     initial = [""]*(stalls+2)
#     initial[0] = "o"
#     initial[len(initial) - 1] = "o"
#     return initial

# def chooseStall(stallList, start, end):
#     chosenStall = (end - start) // 2 + start
#     stallList[chosenStall] = "o"
#     return stallList

# def findGap(stallList):
#     dexO = []
#     for i in range(0, len(stallList)):
#         if stallList[i] == "o":
#             dexO.append(i)
#     maxGap = - 1
#     start, end = 0, 0
#     for num in range(0, len(dexO) - 1):
#         if dexO[num + 1] - dexO[num] > maxGap:
#             start = dexO[num]
#             end = dexO[num + 1]
#             maxGap = dexO[num + 1] - dexO[num]
#     return start, end

# def play(listSize, numPeople):
#     stallList = initialize(listSize)
#     start, end = 0, len(stallList) - 1
#     for num in range(numPeople - 1):
#         stallList = chooseStall(stallList, start, end)
#         start, end = findGap(stallList)
#
#     lastPersonDex = (end - start) // 2 + start
#     Ls = calcLs(stallList, lastPersonDex)
#     Rs = calcRs(stallList, lastPersonDex)
#     return max(Ls, Rs), min(Ls, Rs)





# def initialize(stalls):
#     initial = [""]*(stalls+2)
#     initial[0] = "o"
#     initial[len(initial) - 1] = "o"
#     return initial
#
# def calcLs(stallList, currDex):
#     for num in range(currDex, 0, -1):
#         if stallList[num] == "o":
#             return currDex - num - 1
#     return currDex - 1
#
# def calcRs(stallList, currDex):
#     for num in range(currDex, len(stallList)):
#         if stallList[num] == "o":
#             return num - currDex - 1
#     return len(stallList) - currDex - 2
#
# def playScenario(stallList, people):
#     for person in range(people):
#         personConsiderations = []
#         stallDex = []
#         for i in range(1, len(stallList) - 1):
#             if stallList[i] != "o":
#                 Ls = calcLs(stallList, i)
#                 Rs = calcRs(stallList, i)
#                 personConsiderations.append([Ls, Rs])
#                 stallDex.append(i)
#         minLsRs = -1
#         for consideration in personConsiderations:
#             if min(consideration) > minLsRs:
#                 minLsRs = min(consideration)
#         maxes = []
#         maxDexes = []
#         for s in range(len(stallDex)):
#             if min(personConsiderations[s]) == minLsRs:
#                 maxes.append(personConsiderations[s])
#                 maxDexes.append(s)
#
#         if len(maxes) == 1:
#             stallList[maxDexes[0]] == "o"
#         else:
#             maxLsRs = -1
#             for q in range(len(maxes)):
#                 if (max(maxes[q]) > maxLsRs):
#                     maxLsRs = maxes[q]
#                     chosenStall = maxDexes[q]
#         stallList[chosenStall] = "o"

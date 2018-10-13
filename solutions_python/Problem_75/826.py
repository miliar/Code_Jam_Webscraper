def addToInvokes(currentList,addition,combinedList,opposedList):
    if not currentList == []:
        for combine in combinedList:
            if (addition == combine[0] and currentList[-1] == combine[1]) or (addition == combine[1] and currentList[-1] == combine[0]):
                currentList.pop()
                addToInvokes(currentList,combine[2],combinedList,opposedList)
                return 0

        for opposed in opposedList:
            if (addition == opposed[0] and opposed[1] in currentList) or (addition == opposed[1] and opposed[0] in currentList):
                while not currentList == []:
                    currentList.pop()
                return 0

    currentList.append(addition)

file = open("C:\CodeJam\\QualificationBLarge.in","r")
output = open("C:\CodeJam\\QualificationBLarge.txt","w")

testCases = int(file.readline().strip())

for caseIndex in range(1,testCases+1):
    case = file.readline().strip().split(" ")

    combines = int(case.pop(0))
    combinedInvokes = []
    for combine in range(0,combines):
        combinedInvokes.append(case.pop(0))

    opposed = case.pop(0)
    opposedInvokes = []
    for oppose in range(0,int(opposed)):
        opposedInvokes.append(case.pop(0))

    invokeList = list(case[1])
    invokeResult = []
    invokeResult.append(invokeList.pop(0))

    for invoke in invokeList:
        addToInvokes(invokeResult,invoke,combinedInvokes,opposedInvokes)

    output.write("Case #" + str(caseIndex) + ": " + "[" + ", ".join(invokeResult)+"]")
    if caseIndex != testCases:
        output.write("\n")

output.close()
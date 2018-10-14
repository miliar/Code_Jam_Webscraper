inFile = open("B-large.in")
testCount = int(inFile.readline())

output = []


def DoTrial(elementSeries, combinations, oppositions):
    characterList = []
    for i in range(0, len(elementSeries)):
        characterList.append(elementSeries[i])
        if len(characterList) >= 2:
            for combination in combinations:
                if combination.find(characterList[len(characterList) - 1]) != -1:
                    combo = combination
                    combo = combo.replace(characterList[len(characterList) - 1], "", 1)
                    if characterList[len(characterList) - 2] == combo[0]:
                        del characterList[len(characterList) - 1]
                        characterList[len(characterList) - 1] = combo[1]
        if len(characterList) >= 2 and characterList != []:
            for opposition in oppositions:
                if opposition.find(characterList[len(characterList)- 1]) != -1:
                    localOpposition = opposition
                    localOpposition = localOpposition.replace(characterList[len(characterList)- 1], "", 1)
                    delete = False
                    for character in characterList:
                        if character == localOpposition[0]:
                            delete = True
                            break
                    if delete:
                        characterList = []
                        break

    return characterList



for i in range(0, testCount):
    line = inFile.readline()
    data = line.split(" ")
    combinations = []
    oppositions = []
    elementSeries = ""
    for j in range(0, int(data[0])):
        combinations.append(data[j + 1])
    for j in range(0, int(data[len(combinations) + 1])):
        oppositions.append(data[j + 2 + len(combinations)])
    elementSeries = data[3 + len(combinations) + len(oppositions)].replace("\n", "")
    output.append(DoTrial(elementSeries, combinations, oppositions))



inFile.close()

outFile = open("Output2.out", "w")

caseNumber = 1
for line in output:
    outFile.write("Case #" + str(caseNumber) + ": [" + ", ".join(line) + "]\n")
    caseNumber += 1
outFile.close()
file = open("Google/A-small-attempt0.in", "r")
writeFile = open("out.txt", "w")
list = []
rowRead = 0
firstRightRow = []
secondRightRow = []
for line in file:
    list.append(line.replace('\n', ''))
testCases = int(list[0])
for i in range(0, testCases):
    rowRead +=1
    firstAnswer = int(list[rowRead])
    firstAnswer -= 1
    for j in range(0,4):  
        rowRead +=1
        rowList = list[rowRead].split(' ')
        if j == firstAnswer:
            firstRightRow = rowList
    rowRead += 1
    secondAnswer = int(list[rowRead])
    secondAnswer -= 1
    for j in range(0,4):  
        rowRead +=1
        rowList = list[rowRead].split(' ')
        if j == secondAnswer: 
            secondRightRow = rowList
    sameNumberList = []
    for k in range(0,4):
        for l in range(0,4):
            if firstRightRow[k] == secondRightRow[l]:
                sameNumberList.append(firstRightRow[k])
    if len(sameNumberList) == 1:
        writeFile.write("Case #" + str(i + 1) + ": " + sameNumberList[0] + "\n")
    elif len(sameNumberList):
        writeFile.write("Case #" + str(i + 1) + ": " + "Bad magician!" + "\n")
    else:
        writeFile.write("Case #" + str(i + 1) + ": " + "Volunteer cheated!" + "\n")
file.close()
writeFile.close()

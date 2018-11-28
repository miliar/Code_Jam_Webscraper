inputFile = open("A-small-attempt1.in", "r")
testCaseNum = int(inputFile.readline().replace("\n", ""))

outputFile = open("QRAoutput1", "w")
for testCase in range(1, testCaseNum + 1):
    case_data = inputFile.readline().replace("\n", "").split(" ")
    max_shyness = int(case_data[0])

    people_clapping = 0
    shyness = 0
    friends = 0
    for i in case_data[1]:
        num = int(i)
        if people_clapping < shyness:
            new_friends = (shyness - people_clapping)
            people_clapping += new_friends + num
            friends += new_friends
        else:
            people_clapping += num
        
        if people_clapping >= max_shyness:
            break

        shyness += 1

    outputFile.write("Case #"+str(testCase)+": "+str(friends)+"\n")

inputFile.close()
outputFile.close()

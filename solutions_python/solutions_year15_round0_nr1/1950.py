def a(inputFile):
    opening = open(inputFile, "r")
    output = open("output", "w")
    num = 0
    count = 0
    for line in opening:
        if count == 0:
            num = int(line)
            count += 1
        else:
            splitLine = line.split()
            currCount = 0
            numPeople = 0
            peopleNeeded = 0
            for number in splitLine[1]:
                if currCount > numPeople:
                    peopleNeeded += 1
                    numPeople += 1
                numPeople += int(number)
                currCount += 1
            print("Case #%d: %d" % (count, peopleNeeded), file=output)
            count+=1
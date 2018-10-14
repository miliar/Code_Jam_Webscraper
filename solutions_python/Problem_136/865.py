inputFile = open("B-large.in", "r")
outputFile = open("B-large.out", "w")

testCases = int(inputFile.readline())
caseNumber = 1

for val in range(testCases):
    seconds = []
    totalSeconds = 0

    case = inputFile.readline().split()

    for char in range(len(case)):
       case[char] = float(case[char])
            
    farmPrice = case[0]
    farmRate = case[1]
    goal  = case[2]

    rate = 2.0
    while(True):
        if (goal / rate) > ( (farmPrice / rate) + (goal / (rate + farmRate)) ):
            seconds.append(farmPrice/rate)
            rate += farmRate
        elif (goal / rate) <= ( (farmPrice / rate) + (goal / (rate + farmRate)) ):
            seconds.append(goal / rate)
            break
            
    for char in range(len(seconds)):
        totalSeconds += seconds[char]

    outputFile.write("Case #" + str(caseNumber) + ": " + str(totalSeconds) + "\n")
    caseNumber += 1

inputFile.close()
outputFile.close()

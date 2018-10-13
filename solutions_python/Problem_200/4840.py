inputFile = open('B-small-attempt1.in', 'r')
#inputFile = open('B-small-sample.in', 'r')
outputFile = open('B-small-answer.in', 'w')

entries = int(inputFile.readline())
print(entries)

def CheckNumber(number):
    numString = str(number)
    numList = list(numString)
    numList.sort()
    numOrdered = "".join(numList)
    return numString == numOrdered

def GetAnswer(number):
    while number > 0:
        results = CheckNumber(number)
        if results:
            return str(number)
        number -= 1
    return str(number)

def BuildAnswerFile():
    count = 0
    for line in range(entries):
        count += 1
        currentVal = inputFile.readline()
        if currentVal:
            print("Working with", currentVal)
            answer = GetAnswer(int(currentVal))
            lineAnswer = "Case #" + str(count) + ": " + str(answer) + "\r"
            outputFile.write(lineAnswer)


BuildAnswerFile()
    
outputFile.close()
import sys

if __name__ == '__main__':
    fileInput = open("A-small-attempt0.in", 'r')
    fileOutput = open("output.txt", 'w')

    numCases = int(fileInput.readline())

    for case in range(numCases):
        fileOutput.write("Case #"+str(case+1)+":")
        print("Case #"+str(case+1)+":")

        firstNum = int(fileInput.readline())
        firstArg = list()

        for i in range(4):
            firstArg.append([int(x) for x in fileInput.readline().split()])

        secondNum = int(fileInput.readline())
        secondArg = list()

        for i in range(4):
            secondArg.append([int(x) for x in fileInput.readline().split()])

        accum = 0
        result = -1

        for i in secondArg[secondNum-1]:
            if i in firstArg[firstNum-1]:
                accum += 1
                result = i

        if accum == 0:
            fileOutput.write(" Volunteer cheated!")
        elif accum > 1:
            fileOutput.write(" Bad magician!")
        else:
            fileOutput.write(" "+str(result))

        if case < numCases-1:
            fileOutput.write("\n")

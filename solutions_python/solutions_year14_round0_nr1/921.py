__author__ = 'archeg'

def ComputeMagician():
    pass

def Run(fileName):
    def readArray(f):
        return [int(x) for x in f.readline().split(' ')]

    def readBlock(f):
        firstNumber = int(fi.readline())
        for i in range(firstNumber - 1): fi.readline()
        line = readArray(fi)
        for i in range(4 - firstNumber): fi.readline()
        return line

    def writeCase(i, str):
        return "Case #%i: %s\n" % (i, str)

    outputLines = []
    with open(fileName, 'r') as fi:
        runs = int(fi.readline())
        for i in range(1, runs + 1):
            firstLine = readBlock(fi)
            secondLine = readBlock(fi)

            trickNumbers = [x for x in firstLine if x in secondLine]
            if len(trickNumbers) == 1:
                outputLines.append(writeCase(i, trickNumbers[0]))

            if len(trickNumbers) > 1:
                outputLines.append(writeCase(i, "Bad magician!"))

            if len(trickNumbers) == 0:
                outputLines.append(writeCase(i, "Volunteer cheated!"))
    with open("output.txt", 'w') as fo:
        fo.writelines(outputLines)

Run("input_example.txt")





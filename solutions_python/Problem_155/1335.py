import sys

if __name__ == "__main__":
    inputFile = open(sys.argv[1], 'r')
    testCases = inputFile.readline()
    testCases = int(testCases.rstrip(" \t\n\r"))
    cases = []
    for i in range(0, testCases):
        line = inputFile.readline()
        line = line.rstrip(" \t\n\r")
        parts = line.split(" ")
        case = []
        for j in range(0, int(parts[0])+1):
            case.append(int(parts[1][j]))
        cases.append(case)
    inputFile.close()
    outputFile = open("output.txt", 'w')
    for i in range(0, len(cases)):
        additionalCount = 0
        count = 0
        for j in range(0, len(cases[i])):
            if count < j:
                additionalCount += (j-count)
                count += (j-count)
            count += cases[i][j]
        outputFile.write("Case #" + str(i+1) + ": " + str(additionalCount) + "\n")
    outputFile.close()


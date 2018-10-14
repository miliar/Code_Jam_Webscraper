class FileInput:
    def getFileLines(self, filePath):
        f = open(filePath)

        numCases = f.readline()
        allCases = []

        for index in range(int(numCases)):
            case = self.readCase(f)
            allCases.append(case)

        return allCases

    def readCase(self, file):
        case = []
        paramLine = file.readline()
        paramComponents = paramLine.split()
        numHeight = int(paramComponents[0])

        for index in range(numHeight):
            caseLine = file.readline().strip()
            caseRowComponents = list(caseLine)
            case.append(caseRowComponents)
        return case




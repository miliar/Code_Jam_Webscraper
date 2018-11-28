class OutputText:
    def __init__(self, inputFile):
        self.inputFile = open(inputFile, "w+")
        self.inputFile.truncate()
        self.case = 0

    def addToFile(self, inputValue, outputType):
        self.case += 1
        if outputType == str:
            self.inputFile.write("Case #%d: %s\n" % (self.case, inputValue))
        elif outputType == int:
            self.inputFile.write("Case #%d: %d\n" % (self.case, inputValue))
        elif outputType == float:
            self.inputFile.write("Case #%d: %f\n" % (self.case, inputValue))

    def allDone(self):
        self.inputFile.close()

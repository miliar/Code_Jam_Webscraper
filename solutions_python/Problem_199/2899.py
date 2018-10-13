import sys

class PancakeFlipper(object):

    def _allPancakesSmiley(self, pcRow):
        outVal = True
        if "-" in pcRow:
            outVal = False
        return outVal

    def _makeStringArray(self, myString):
        outVal = []
        for i in range(0, len(myString), 1):
            outVal.append(myString[i])
        return outVal
    
    def getNumberOfFlips(self, pcRow, flipSize):
        outVal = ""
        flipCount = 0
        arrayRow = self._makeStringArray(pcRow)
        while len(arrayRow) > 0 and int(flipSize) <= len(arrayRow):
            if arrayRow[0] == "+":
                arrayRow.pop(0)
            else:
                flipCount += 1
                for i in range(0, int(flipSize), 1):
                    if arrayRow[i] == "+":
                        arrayRow[i] = "-"
                    else:
                        arrayRow[i] = "+"    
        if arrayRow[0] == "-":
            outVal = "IMPOSSIBLE"
        else:
            if self._allPancakesSmiley(arrayRow):
                outVal = str(flipCount)
            else:
                outVal = "IMPOSSIBLE"
        return outVal

def main():
    pc_index = 0
    size_index = 1
    myFizzle = open(sys.argv[1], "r")
    loadedFile = []
    numberOfTestCases = int(myFizzle.readline())
    myLine = myFizzle.readline()
    while myLine:
        myTokens = myLine.strip().split(" ")
        loadedFile.append((myTokens[pc_index], myTokens[size_index]))
        myLine = myFizzle.readline()
    myFizzle.close()
    myFizzle = open("results.txt", "w")
    pf = PancakeFlipper()
    for i in range(0, numberOfTestCases, 1):
        myFizzle.write("Case #" + str(i + 1) + ":  " + pf.getNumberOfFlips(loadedFile[i][pc_index], loadedFile[i][size_index]) + "\n")
    myFizzle.close()

main()
    

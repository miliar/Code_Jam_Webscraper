import sys

class TidyNumber(object):

    def _concatenateResultAndTemp(self, rArray, tArray):
        outVal = rArray
        for i in range(0, len(tArray), 1):
            outVal.append(tArray[i])
        return outVal

    def _decrementValuesInArray(self, theArray):
        for i in range(0, len(theArray), 1):
            if i == 0:
                theArray[i] = str(int(theArray[i]) - 1)
            else:
                theArray[i] = "9"
        return theArray
    
    def _makeArrayNumber(self, theArray):
        outVal = ""
        for i in range(0, len(theArray), 1):
            outVal += theArray[i]
        return outVal
    
    def _makeNumberArray(self, theNumber):
        outVal = []
        for i in range(0, len(theNumber), 1):
            outVal.append(theNumber[i])
        return outVal
    
    def _numberIsNotTidy(self, theNumber):
        if len(theNumber) == 1:
            return False
        else:
            if int(theNumber[0]) <= int(theNumber[1]):
                if len(theNumber) == 2:
                    return False
                else:
                    return self._numberIsNotTidy(theNumber[1:])
            else:
                return True

    def _removeLeadingZeros(self, myDigits):
        if len(myDigits) > 1:
            if myDigits[0] == "0":
                return self._removeLeadingZeros(myDigits[1:])
            else:
                return myDigits
        else:
            return myDigits
        
    def getLastTidyNumber(self, theNumber):
        outVal = theNumber
        if len(theNumber) != 1:
            while self._numberIsNotTidy(outVal):
                arrayNumber = self._makeNumberArray(outVal)
                foundGreaterNumber = False
                resultingArray = []
                for i in range(0, len(arrayNumber), 1):
                    if i + 1 < len(arrayNumber):
                        if int(arrayNumber[i]) > int(arrayNumber[i + 1]):
                            foundGreaterNumber = True
                            tempArray = self._decrementValuesInArray(arrayNumber[i:len(arrayNumber)])
                            resultingArray = self._concatenateResultAndTemp(resultingArray, tempArray)
                        else:
                            resultingArray.append(arrayNumber[i])
                    else:
                        resultingArray.append(arrayNumber[i])
                    if foundGreaterNumber:
                        break
                outVal = self._makeArrayNumber(self._removeLeadingZeros(resultingArray))
        return outVal

def main():
    myFizzle = open(sys.argv[1], "r")
    loadedFile = []
    numberOfTestCases = int(myFizzle.readline())
    myLine = myFizzle.readline()
    while myLine:
        loadedFile.append(myLine.strip())
        myLine = myFizzle.readline()
    myFizzle.close()
    myFizzle = open("results.txt", "w")
    tn = TidyNumber()
    for i in range(0, numberOfTestCases, 1):
        myFizzle.write("Case #" + str(i + 1) + ":  " + tn.getLastTidyNumber(loadedFile[i]) + "\n")
    myFizzle.close()

main()
    

import copy

class CaseFile(file):
    def getCaseNumber(self):
        if not hasattr(self, 'caseNumber'):
            self.caseNumber = 1
        else:
            self.caseNumber += 1
        return self.caseNumber

    def writeCaseResult(self, result):
        caseNumber = self.getCaseNumber()
        outputText = "Case #"+ str(caseNumber) + ": " + str(result) + "\n"
        self.write(outputText)
    
def readIntegerFromFileLine(tFile):
    return int(tFile.readline().strip())
    
def readLineFromFile(tFile):
    return tFile.readline().strip()


def buildMapping(inputFile, outputFile):
    tInFile = open(inputFile)
    tOutFile = open(outputFile)
    
    cases = readIntegerFromFileLine(tInFile)
    
    mapping = {}
    for caseNumber in range(cases):
        lineTextGooglerese = readLineFromFile(tInFile)
        outputCaseLine = readLineFromFile(tOutFile)
        lineEnglish = outputCaseLine[outputCaseLine.find(':')+1:].strip()
        
        print lineEnglish
        for counter in range(len(lineTextGooglerese)):
            if lineTextGooglerese[counter] != " ":
                mapping[lineTextGooglerese[counter]] = lineEnglish[counter]
                
    mapping["q"] = "z"
    
        
    alphabetSet = set()
    for charC in range(ord('a'),ord('z')+1):
        alphabetSet.add(chr(charC))
        
    cAlphabetSet = copy.deepcopy(alphabetSet)
    
    print alphabetSet
    for character in mapping.keys():
        alphabetSet.remove(character)
        
    print alphabetSet
    
    for character in mapping.values():
        cAlphabetSet.remove(character)
    
    print cAlphabetSet
    
    mapping[alphabetSet.pop()] = cAlphabetSet.pop()
    
    print "Number of keys", len(mapping.keys())
    print mapping
    return mapping

def translateLang(mapping, inputFile, outputFile):
    tInFile = open(inputFile)
    tOutFile = CaseFile(outputFile, 'w')
    
    cases = readIntegerFromFileLine(tInFile)
    
    for caseNumber in range(cases):
        lineTextGooglerese = readLineFromFile(tInFile)
        lineEnglish = ""
        for character in lineTextGooglerese:
            if character != " ":
                lineEnglish = lineEnglish + mapping[character]
            else:
                lineEnglish = lineEnglish + " "
        tOutFile.writeCaseResult(lineEnglish)
    
if __name__ == "__main__":
    googlereseMapping = buildMapping('./input.txt', './output.txt')
    
    translateLang(googlereseMapping, './input.txt','testOutput.txt')
    translateLang(googlereseMapping, './A-small-attempt0.in','./A-small-attm0.out')
    
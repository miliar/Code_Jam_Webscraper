class LangDict ( object ):

    def __init__(self, length):
        self.charMapper = []
        self.wordHash = {}
        for i in range(0,length):
            self.charMapper.append({})

    def addWord(self, word):
        assert len(word) == len(self.charMapper)
        self.wordHash[word] = True
        for i in range(0,len(self.charMapper)):
            if word[i] in self.charMapper[i]:
                self.charMapper[i][word[i]][word] = True
            else:
                self.charMapper[i][word[i]] = {}
                self.charMapper[i][word[i]][word] = True

    def getNumWords(self, wordPattern):
        pattern = self.parseWordPattern(wordPattern)

        finalSet = None

        assert len(pattern) == len(self.charMapper)
        
        for i in range(0,len(pattern)):
            charData = pattern[i]
            thisSet = {}
            for char in charData:
                if char in self.charMapper[i]:
                    thisSet = self.unionDicts(thisSet, self.charMapper[i][char])
            if finalSet == None:
                finalSet = thisSet
            else:
                finalSet = self.intersectDicts(thisSet, finalSet)

        return len(finalSet)

    def parseWordPattern(self, wordPattern):
        wordPattern = wordPattern.replace("(","|(").replace(")",")|")
        parseStepList = wordPattern.split("|")
        wordPatternList = []
        for charStr in parseStepList:
            if len(charStr)==0: continue
            if charStr[0] == "(":
                wordPatternList.append(charStr[1:-1])
            else:
                for ch in charStr:
                    wordPatternList.append(ch)
        return wordPatternList

    def intersectDicts(self, dict1, dict2):
        result = {}
        for word in dict1:
            if word in dict2:
                result[word] = True
        return result

    def unionDicts(self, dict1, dict2):
        result = {}
        for word in dict1:
            result[word] = True
        for word in dict2:
            result[word] = True
        return result



def makeDict(filename):
    f = open(filename)
    of = open("out.txt",'w')
    firstLine = f.readline()

    langDict = LangDict(int(firstLine.split(" ")[0]))
    numWords = int(firstLine.split(" ")[1])
    numTests = int(firstLine.split(" ")[2])

    for i in range(0,numWords):
        langDict.addWord(f.readline()[:-1])

    for i in range(0,numTests):
        of.write("Case #%d: %d\n" % (i+1,langDict.getNumWords(f.readline()[:-1])))

    f.close()

makeDict('intext.txt')

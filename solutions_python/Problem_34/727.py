import re

inputLinePattern = re.compile("\d+ \d+ \d+")
def parseLines(file):
    (length, numWords, numPatterns) = file.next().split()
    
    words = []
    for i in range(int(numWords)):
        words.append(file.next())
                
    patterns = []
    patternStrings = []
    for i in range(int(numPatterns)):
        patternString = parsePatternLine(file.next())
        patterns.append(re.compile(patternString))
        patternStrings.append(patternString)
    caseNumber = 1
    for pattern in patterns:
        count = 0
        for word in words:
            if pattern.match(word):
                count += 1
        print "Case #" + str(caseNumber) + ": " + str(count)
        caseNumber += 1
    parseLines(file)
    
wordPattern = re.compile("\w+")
def parsePatternLine(line):
    return line.replace("(", "[").replace(")","]")

file = open("input")
try:
    parseLines(file)
except: pass

import string


langString = "yhesocvxduiglbkrztnwjpfmaq "
langDict = dict(zip(string.ascii_lowercase+' ', langString))

def transLetter(aChar):
    return langDict[aChar]

def transLine(aLine):
    result = ''
    for char in aLine.lower():
        result += transLetter(char)
    return result

def readCase(theFile):
    return theFile.readline().strip()

def writeCase(theFile, caseNumber, answer):
    theLine = "Case #%d: %s"%(caseNumber, answer)
    theFile.write(theLine + "\n")
    return

def solveCase(aLine):
    return transLine(aLine)

def main(fileName):
    f = open(fileName+".in", "U")
    g = open(fileName+".out", "w")
    cases = int(f.readline())
    for x in xrange(cases):
        writeCase(g, x+1, solveCase(readCase(f)))
    f.close()
    g.close()
    return

if __name__ == "__main__":
    from sys import argv
    main(argv[1])

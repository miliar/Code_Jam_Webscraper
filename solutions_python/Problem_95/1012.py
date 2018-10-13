def speaking_in_tongues():
    inputFile = open('input.txt','r')
    outputFile = open('output.txt','w')
    numTestCases = int(inputFile.readline())
    letterMap = parseLetterMapping()
    for tc in range(0,numTestCases):
        inputString = inputFile.readline().rstrip()
        inputString = list(inputString)
        outputString = ''
        for i in range(0,len(inputString)):
            if inputString[i] == ' ':
                outputString += ' '
            else:
                outputString += letterMap[inputString[i]]
        outputString = 'Case #%d: %s\n'%(tc+1,outputString)
        outputFile.write(outputString)
        
def parseLetterMapping():
    letterMap = {}
    inputString = []
    inputString.append('ejp mysljylc kd kxveddknmc re jsicpdrysi')
    inputString.append('rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd')
    inputString.append('de kr kd eoya kw aej tysr re ujdr lkgc jv')
    inputString.append('y qee')
    outputString = []
    outputString.append('our language is impossible to understand')
    outputString.append('there are twenty six factorial possibilities')
    outputString.append('so it is okay if you want to just give up')
    outputString.append('a zoo')
    
    for i in range(0,len(inputString)):
        inputStringSplit = list(inputString[i])
        outputstringSplit = list(outputString[i])
        for j in range(0,len(inputStringSplit)):
            if inputStringSplit[j] != ' ':
                letterMap[inputStringSplit[j]] = outputstringSplit[j]
    
    letterMap['z'] = 'q'
    
    return letterMap
            
if __name__ == '__main__':
    speaking_in_tongues()
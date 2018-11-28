myKeyValDict = {"a" : "y","b" : "h","c" : "e","d" : "s","e" : "o","f" : "c","g" : "v",
                "h" : "x","i" : "d","j" : "u","k" : "i",
                "l" : "g","m" : "l","n" : "b","o" : "k","p" : "r",
                "q" : "z","r" : "t","s" : "n","t" : "w","u" : "j",
                "v" : "p","w" : "f","x" : "m","y" : "a","z" : "q"}

fileHandler = open('A-small-attempt0.in', 'r')
allLines = fileHandler.readlines()
fileHandler.close()

print allLines
newLineList = []
newVal = ''
newLine = ' '
case = 0
#print listOfLines
for line in allLines:
    line = line.rstrip()
    listOfLine = line.split()
    for val in listOfLine:
        #print "Value is "+val
        for character in val:
            if myKeyValDict.has_key(character):
                engValue = myKeyValDict[character]
                #newVal = val.replace(character, engValue)
                #val = newVal
                newVal = newVal + engValue
        newLineList.append(newVal)
        newVal = ''
        #print "replaced value is "
        #print newLineList
    newLine = ' '.join(newLineList)
    print newLine
    newLineList = []
    if newLine != '':
        case = case + 1
        caseNumber = 'Case #'+str(case)
        newFileHandler = open('output.txt', 'a')
        newFileHandler.write(caseNumber)
        newFileHandler.write(':\t')
        newFileHandler.write(newLine)
        newFileHandler.write('\n')
        
        
    #newLineList.append(val)
    #print newLineList

    #newLine = ' '.join(newLineList)
    #ssprint newLine
    

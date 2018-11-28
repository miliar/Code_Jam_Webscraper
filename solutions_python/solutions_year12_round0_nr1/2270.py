# Google competition
# Qualifiers

inputList = []
translatedList = []

translateDict = {
    'a' : 'y',
    'b' : 'h', #or z
    'c' : 'e',
    'd' : 's',
    'e' : 'o',
    'f' : 'c',
    'g' : 'v',
    'h' : 'x',
    'i' : 'd',
    'j' : 'u',
    'k' : 'i',
    'l' : 'g',
    'm' : 'l',
    'n' : 'b',
    'o' : 'k',
    'p' : 'r',
    'q' : 'z',#or h
    'r' : 't',
    's' : 'n',
    't' : 'w',
    'u' : 'j',
    'v' : 'p',
    'w' : 'f',
    'x' : 'm',
    'y' : 'a',
    'z' : 'q' }

def parseInput( filename ):
    fd = open( filename )

    

    for line in fd:
        line = line.strip('\n')
        wordList = line.split(' ')
        inputList.append( wordList )

    inputList.pop(0)

    fd.close()

def translateInput( inList ):
    for line in inList:
        newLine = []
        for word in line:
            newWord = ""
            for char in word:
                newWord += translateDict[char]
            newLine.append( newWord )
        translatedList.append( newLine )
        
def outputTranslation( translation ):
    for i in range(0, len(translation) ):
        outputLine = "Case #" + str(i+1) + ": "
        for word in translation[i]:
            outputLine += word
            if i != len(translation[i]) - 1:
                outputLine += " "
        print( outputLine )
                   
    

parseInput( "test.txt" )
translateInput( inputList )
outputTranslation( translatedList )

import os
os.chdir("D://")


def openDataFile(filename):
    return open(filename)

def shipLater(stringToShip,numberShip):
    testAfterShip = ''
    for letter in stringToShip:
        if letter != ' ':
            testAfterShip+=convertSmallLetter(letter,numberShip)
        else:
            testAfterShip+=letter
    return testAfterShip

def convertSmallLetter(letter,shipNumber):
    asciiLertter = ord(letter)
    if (asciiLertter + shipNumber) > 122:
        shipNumber = (asciiLertter + shipNumber) - 122
        return convertSmallLetter('a',shipNumber-1)
    else:
        return chr(ord(letter)+shipNumber) 


def testShipAllIndex(word):
    for i in range(24):
        print("Index Ship is : ",('1'))
        print("\n word is :",shipLater(word,i+1))


def getIndexShip(letter1,letter2):
    for i in range (24):
        if convertSmallLetter(letter1,i+1) == letter2:
            return i+1
        
def findShipLetterFromWord(wordNotShip,wordShip):
    dictShip = {}
    for letter1,letter2 in zip(wordShip,wordNotShip):
        #print letter1,letter2
        if letter1 not in dictShip:
            if(letter1 != ' '):
                indexShip = getIndexShip(letter1,letter2)
                dictShip[letter1] = letter2;
            
    return dictShip

def convertWord(mapWord,word):
    newWord = ''
    for letter in word:
        if letter != ' ' and letter != '\n':
            newWord+=mapWord[letter]
        else:
            newWord+=' '
    return newWord



def mainTask():
    mapLetter = {'q':'z','z':'q','a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm'}
    dataFile = openDataFile('A-small-attempt2.in');
    amountCase = int(dataFile.readline())
   
    numberCase = 1
    for line in dataFile:
        reulst = 'Case #'+str(numberCase)+': '+convertWord(mapLetter,line)
        print(reulst)
        numberCase+=1
    dataFile.close()













    

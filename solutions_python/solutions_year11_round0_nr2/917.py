# The basic idea is that you add element-after-element and check 2 conditions

allCombinations=[]
allOppose=[]

def runTestCase(sequence):
    global allCombinations
    global allOppose
    sequence=sequence.split()

    # Parsing combination knowledge
    noOfCombiningElements=int(sequence[0])
    combinationSeq=sequence[1:noOfCombiningElements+1]
    for seq in combinationSeq:
        allCombinations.append(seq)
    sequence=sequence[noOfCombiningElements+1:]
    
    # Parsing opposition knowledge
    noOfOpposingElements=int(sequence[0])
    opposingSeq=sequence[1:noOfOpposingElements+1]
    for seq in opposingSeq:
        allOppose.append(seq)
    sequence=sequence[noOfOpposingElements+1:]

    sequence=sequence[1:] # Getting rid of extra info
    elementList=[]
    for char in sequence[0]:
        elementList.append(char)
        # The actual magic lies here
        if(len(elementList)==1):
            continue
        myString=elementList[-1]+elementList[-2]
        output=combinationSubst(myString)
        if(output):
            elementList=elementList[:-2]
            elementList.append(output)
        else:
            if(opposingElementsPresent(elementList[-1],elementList[:-1])):
                elementList=[]
    return elementList

def opposingElementsPresent(element,elementList):
    for existingElement in elementList:
        myString=existingElement+element
        answer=opposingSubst(myString)
        if(answer):
            return answer
    return False

def opposingSubst(myString):
    for seq in allOppose:
        if(seq==myString or seq==invertString(myString)):
            return True
    return False

def invertString(twoCharString):
    newString=twoCharString[1]
    newString=newString+twoCharString[0]
    return newString

def combinationSubst(myString):
    for seq in allCombinations:
        if(seq.startswith(myString) or seq.startswith(invertString(myString))):
            return seq[-1]
    return None

def runner(fileName):
    global allCombinations
    global allOppose
    fileHandle=open(fileName)
    noOfCases=fileHandle.readline()
    for n in range(1,int(noOfCases)+1):
        sequence=fileHandle.readline()
        allCombinations=[]
        allOppose=[]
        print "Case #"+str(n)+": "+prepareFinalList(runTestCase(sequence))

def prepareFinalList(myList):
    finalString="["
    for element in myList:
        if(len(finalString)==1):
            finalString=finalString+element
        else:
            finalString=finalString+", "+element
    finalString=finalString+"]"
    return finalString
    
        

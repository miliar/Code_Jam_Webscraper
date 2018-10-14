
INPUT_FILE = 'warInput.txt'
OUTPUT_FILE = 'warOutput.txt'

def warFunction():
    inputFile = open(INPUT_FILE, 'r')
    outputFile = open(OUTPUT_FILE, 'w')
    noTestCase = int(inputFile.readline())
    
    for i in xrange(noTestCase):
        outputLine =  "Case #" + str(i+1) + ": "
        
        
        weighNo = int(inputFile.readline())
        #read Naomi's weigh
        NWeighList = []
        count = 0
        theLine = inputFile.readline()
        while len(NWeighList) < weighNo:
            word = ""
            while theLine[count] != " " and theLine[count] != "\n":
                word += theLine[count]
                count += 1
            else:
                NWeighList.append(float(word))
            count += 1
                
        #read Ken's weigh
        KWeighList = []
        count = 0
        theLine = inputFile.readline()
        while len(KWeighList) < weighNo:
            word = ""
            while theLine[count] != " " and theLine[count] != "\n":
                word += theLine[count]
                count += 1
            else:
                KWeighList.append(float(word))
            count += 1
        
        NWeighList.sort()
        KWeighList.sort()
        
        deceitfulScore = deceitfulAlgo(NWeighList, KWeighList)
        normalScore = normalAlgo(NWeighList, KWeighList)
        
        outputLine += str(deceitfulScore) + " " + str(normalScore)
        outputFile.write(outputLine + '\n')


def deceitfulAlgo(NWeighList, KWeighList):
    weighNo = len(NWeighList)
    tempList = []
    for element in KWeighList:
        tempList.append(element)
    for i in xrange(weighNo):
        if NWeighList[i] > tempList[0]:
            tempList.remove(tempList[0])
    
    return weighNo - len(tempList)

def normalAlgo(NWeighList, KWeighList):
    weighNo = len(NWeighList)
    tempList = []
    for element in NWeighList:
        tempList.append(element)
    for i in xrange(weighNo):
        if KWeighList[i] > tempList[0]:
            tempList.remove(tempList[0])

    return len(tempList)

if __name__ == '__main__':
    warFunction()
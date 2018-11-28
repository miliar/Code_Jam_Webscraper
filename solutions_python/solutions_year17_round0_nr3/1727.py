def calcVals(pos, stallArray):
    Ls = 0
    Rs = 0
    for i in range(pos-1, -1, -1):
        if (stallArray[i] == True):
            break
        Ls += 1
    for i in range(pos+1, len(stallArray)):
        if (stallArray[i] == True):
            break
        Rs += 1    

    return(max(Ls,Rs), min(Ls,Rs))

def placePerson(stallArray):
    emptiesPos = 0
    emptiesLength = 0
    tempPos = 0
    tempLength = 0
    startCounting = True
    
    for i in range(0, len(stallArray)):
        if (stallArray[i] == False) & (startCounting == True):
            tempPos = i
            tempLength += 1
            startCounting = False
        elif (stallArray[i] == False) & (startCounting == False):
            tempLength += 1
        elif (stallArray[i] == True):
            startCounting = True
            if (emptiesLength < tempLength):
                emptiesPos = tempPos
                emptiesLength = tempLength
            tempLength = 0;
        if (stallArray[i] == False) & (i == len(stallArray)-1):
            if (emptiesLength < tempLength):
                emptiesPos = tempPos
                emptiesLength = tempLength
    
    if (emptiesLength == 1):
        stallArray[emptiesPos] = True
        return emptiesPos
    elif (emptiesLength % 2 == 0):
        stallArray[emptiesPos + int(emptiesLength / 2) - 1] = True
        return emptiesPos + int(emptiesLength / 2) - 1
    elif (emptiesLength % 2 == 1):
        stallArray[emptiesPos + int(emptiesLength / 2)] = True
        return emptiesPos + int(emptiesLength / 2)

f = open('data.txt', 'r')
array = f.readlines()

for i in range(0,len(array)):
     array[i] = array[i].strip()

testNum = int(array[0])
array.pop(0)

for i in range(0, testNum):
    maxVal = 0
    minVal = 0
    innerArray = array[i].split(" ")
    n = innerArray[0]
    k = innerArray[1]

    stallArray = [False] * int(n)

    for j in range(0, int(k)):                
        pos = placePerson(stallArray)
        if (j == int(k) - 1):
            (maxVal, minVal) = calcVals(pos, stallArray)
    
    print("Case #" + str(i+1) + ": " + str(maxVal) + " " + str(minVal))



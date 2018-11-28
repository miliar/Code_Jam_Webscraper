def tidy(num):
    lastChar = ord(num[0])
    for j in range(1, len(num)):
        if (lastChar > ord(num[j])):
            return False
        else:
            lastChar = ord(num[j])
    return True

f = open('data.txt', 'r')
array = f.readlines()

for i in range(0,len(array)):
     array[i] = array[i].strip()

testNum = int(array[0])
array.pop(0)

for i in range(0, testNum):
    tidyNum = 0
    maxValue = int(array[i])
    stringMaxValue = str(maxValue)
        
    lastChar = ord(stringMaxValue[0])
    cutPos = -1
    cutPosTwo = -1
    storeTwo = True
    for j in range(1, len(stringMaxValue)):
        if (lastChar > ord(stringMaxValue[j])):
            cutPos = j
            break
        elif (lastChar == ord(stringMaxValue[j])) & (storeTwo):
            cutPosTwo = j
            storeTwo = False
        elif (lastChar < ord(stringMaxValue[j])):
            lastChar = ord(stringMaxValue[j])
            storeTwo = True

    if (cutPos == -1):
        tidyNum = maxValue
    else:
        numToCut = int(stringMaxValue[cutPos:])
        tidyNum = maxValue - numToCut - 1
        if (tidy(str(tidyNum)) != True):
            numToCut = int(stringMaxValue[cutPosTwo:])
            tidyNum = maxValue - numToCut - 1
    
    print("Case #" + str(i+1) + ": " + str(tidyNum))
    



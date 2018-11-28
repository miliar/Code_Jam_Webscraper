def printOutput(caseNum, result):
    output = "Case #%d: %d" % (caseNum, result)
    print(output)

def isIncreasing(num):

    listNum = list(str(num))
    
    if len(listNum) == 1:
        return True
    
    for i in range(len(listNum)-1):
        if listNum[i] > listNum[i+1]:
            return False
    return True

def findLastIncrease(listNum):

    index = 0
    for i in range(len(listNum)-1):
        if listNum[i] < listNum[i+1]:
            index = i+1
    return index
    
    
numCases = int(input())
for i in range(1, numCases + 1):
    num = int(input())
    listNum = list(str(num))
    
    index = findLastIncrease(listNum)

    if not isIncreasing(num):
        number = int(listNum[index])
        number -= 1
        listNum[index] = str(number)

        for j in range(index+1, len(listNum)):
            listNum[j] = '9'
                
        strNum = ""
        for s in listNum:
            strNum += s
        num = int(strNum)
            


        while not isIncreasing(num):
            num -= 1
                
    
    
    printOutput(i, num)
            
    




#!/usr/bin/env python
#coding=utf-8

def PrintCase(caseNo, result):
    tmp = "Case #" + str(caseNo) + ": " + str(result) + '\n'
    return tmp

def generateArrangeByTotalPoints(total):
    possibleList = []

    for i in range(0, 11):
        for j in range(0, 11):            
            for k in range(0, 11):
                if (i + j + k) == total :
                    tmpList = [i, j, k]
                    tmpList = sorted(tmpList)
                    
                    if tmpList[2] - tmpList[0] <= 2:
                            bExist = False
                            for tmpExistList in possibleList:
                                if tmpExistList[0] == tmpList[0] \
                                    and tmpExistList[1] == tmpList[1] \
                                    and tmpExistList[2] == tmpList[2]:
                                    bExist = True
                                    break
                            
                            if bExist == False :
                                possibleList.append(tmpList)
                    
    return possibleList

def isSuprisingCase(listOfPoints):
    
    if listOfPoints[2] - listOfPoints[0] == 2:
        return True
    else :
        return False

def NestedComputePosListByNoOfSuprisingCase(possibleArrangeOfAllteam,
                                            NoOfNested,
                                            pointOfBest,
                                            noOfEmployee,
                                            noOfSuprisingCase,
                                            curNoOfSuprisingCase,
                                            curPointList):

    if NoOfNested == noOfEmployee:
        if noOfSuprisingCase == curNoOfSuprisingCase:
            func_NoOfBest = 0
            for tmpList in curPointList:
                if tmpList[2] >= pointOfBest:
                    func_NoOfBest += 1
                    
            global maxOfBestNo
            global sucessOfThisLine
            
            if maxOfBestNo < func_NoOfBest :
                maxOfBestNo = func_NoOfBest;
            
            if sucessOfThisLine == False :
                sucessOfThisLine = True
            
        return
    
    for tmpList in possibleArrangeOfAllteam[NoOfNested]:
        if isSuprisingCase(tmpList) == True:
            func_CurNoOfSuprisingCase = curNoOfSuprisingCase + 1
        else :
            func_CurNoOfSuprisingCase = curNoOfSuprisingCase
            
        curPointList.append(tmpList)
        NestedComputePosListByNoOfSuprisingCase(possibleArrangeOfAllteam,
                                                                        NoOfNested + 1,
                                                                        pointOfBest,
                                                                        noOfEmployee,
                                                                        noOfSuprisingCase,
                                                                        func_CurNoOfSuprisingCase,
                                                                        curPointList)

        del curPointList[NoOfNested]
        

def findNoOfBest(possibleArrangeOfAllteam, pointOfBest, noOfSuprisingCase, noOfEmployee):
    
    return  NestedComputePosListByNoOfSuprisingCase(possibleArrangeOfAllteam, 0, pointOfBest, noOfEmployee, noOfSuprisingCase, 0, [])

def main(fileName):
    
    file = open(fileName, 'r')
    i = 0
    resStr = ''
    for tmpContext in file.readlines():
        if i == 0 :
            i += 1
            continue
        tmpContextArrange = tmpContext.split()
        noOfEmployee = int(tmpContextArrange[0])
        noOfSuprisingCase = int(tmpContextArrange[1])
        pointOfBest = int(tmpContextArrange[2])
        
        j = 0
        possibleArrangeOfAllteam = []
        for j in range(0, noOfEmployee):
            possibleArrangeOfAllteam.append(generateArrangeByTotalPoints(int(tmpContextArrange[j + 3])))
            j += 1
            
        global maxOfBestNo
        global sucessOfThisLine
        
        maxOfBestNo = 0
        sucessOfThisLine = False
        
        findNoOfBest(possibleArrangeOfAllteam, pointOfBest, noOfSuprisingCase, noOfEmployee)
        
        if sucessOfThisLine == False :
            print 'It is impossible :( -_-!'
            return
        
        resStr += PrintCase(i, maxOfBestNo)
        i += 1
    
    print resStr
    
    resultFile = open('a.out', 'w')
    resultFile.write(resStr)
    resultFile.close()
    file.close()
    
maxOfBestNo = 0
sucessOfThisLine = False

if __name__ == '__main__':
    
    main('B-small-attempt0.in')
    


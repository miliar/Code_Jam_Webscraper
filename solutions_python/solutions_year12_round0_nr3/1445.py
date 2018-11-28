#!/usr/bin/env python
#coding=utf-8

def PrintCase(caseNo, result):
    tmp = "Case #" + str(caseNo) + ": " + str(result) + '\n'
    return tmp

def GeneratePair(numA, numB, strCurNo):
    global thisLineIsRN
    global thisLineSelectedSet
    
    curNo = int(strCurNo)
    for i in range(0, len(strCurNo) - 1) :
        tmpStr = strCurNo[(i + 1):len(strCurNo)] + strCurNo[0:(i + 1)]
        newNo = int(tmpStr)
        #print 'newNo', newNo
        
        if newNo in thisLineSelectedSet:
            #print "No need -->", newNo
            continue
        
        if (numA <= newNo) and (numB >= newNo) and (newNo != curNo):
            thisLineIsRN.append([curNo, newNo])
            thisLineSelectedSet.add(curNo)
            #thisLineSelectedSet.add(newNo)
            #print "### found :", newNo
            #print "### found Pair No:", len(thisLineIsRN)
            #print thisLineIsRN
            #break
        
        elif newNo == curNo :
            break


def ComputeRecycledNumber(A, B):
    numA = int(A)
    numB = int(B)
    
    lenB = len(B)
    lenA = len(A)
    if lenA == 1 and lenB == 1:
        return 0

    for i in range(numA, numB + 1):
        strCurNo = str(i)
        #print 'i :', i
        GeneratePair(numA, numB, strCurNo)
        #print '<--- --->'

def main(fileName):
    
    file = open(fileName, 'r')
    i = 0
    resStr = ''
    for tmpContext in file.readlines():
        if i == 0 :
            i += 1
            continue
        #print tmpContext
        tmpContextArrange = tmpContext.split()
        A = tmpContextArrange[0]
        B = tmpContextArrange[1]
            
        global thisLineIsRN
        global thisLineSelectedSet
        
        thisLineIsRN = list()
        thisLineSelectedSet = set()
        ComputeRecycledNumber(A, B)
        
        resStr += PrintCase(i, len(thisLineIsRN))
        i += 1
        #print thisLineIsRN
        #for tmp in list(thisLineIsRN):
        #    print tmp
        del thisLineIsRN
        del thisLineSelectedSet
        
    print resStr
    
    resultFile = open('a.out', 'w')
    resultFile.write(resStr)
    resultFile.close()
    file.close()
    
thisLineIsRN = []
thisLineSelectedSet = set()

if __name__ == '__main__':
    
    main('C-small-attempt0.in')
    


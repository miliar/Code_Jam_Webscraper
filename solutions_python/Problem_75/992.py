#!/usr/bin/env python3.1

baseElements = ('Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F')

def isCombination(first, second, combinations):
    """
    
    
    first -- first element to see if is a combination   
    second -- second element to see if is a combination  
    """
    if first in baseElements:
        if second in baseElements:
            for i in range(len(combinations)):
                if first in combinations[i]:
                    if first is combinations[i][0]:
                        if second is combinations[i][1]:
                            return combinations[i][2]
                    else:
                        if second is combinations[i][0]:
                            return combinations[i][2]
    return None

def hasOpposedElements(elementList, opposedElements):
    """
    
    
    elementList -- element List to see if there is opposed elements
    opposedElements -- list of elements that are opposed
    """
    for c in elementList:
        if c in baseElements:
            for i in range(len(opposedElements)):
                if c in opposedElements[i]:
                    if c is opposedElements[i][0]:
                        if opposedElements[i][1] in elementList:
                            return True
                    else:
                        if opposedElements[i][0] in elementList:
                            return True
            else:
                elementList = elementList[1:]
    return False


        

with open('B-large.in', 'r') as f:
    line = f.readline()
    intT = int(line)
    for case in range(1, intT + 1):
        line = f.readline()
        fields = line.split()
        i = 0
        intC = int(fields[i])
        strC = []
        i = i + 1
        for iC in range(intC):
                strC.append(fields[i])
                i = i + 1
        intD = int(fields[i])
        strD = []
        i = i + 1
        for iD in range(intD):
                strD.append(fields[i])
                i = i + 1
        intN = int(fields[i])
        i = i + 1
        if intN is not 0:
            strN = fields[i]
            elementsList = strN[0]
            for e in range(1, intN):
                elementsList = elementsList + strN[e]
                nElements = len(elementsList)
                if nElements > 1:
                    comb = isCombination(elementsList[nElements-2], elementsList[nElements-1], strC)
                    if comb is not None:
                        elementsList = elementsList[:-2] + comb
                    else:
                        opps = hasOpposedElements(elementsList, strD)
                        if opps is True:
                            elementsList = ''
        print('Case #{0}: ['.format(case), end='')
        nElements = len(elementsList)
        for j in range(nElements):
            print(elementsList[j], end='')
            if j is not nElements - 1:
                print(', ', end='')
        print(']')

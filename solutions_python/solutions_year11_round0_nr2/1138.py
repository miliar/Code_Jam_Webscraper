# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="ozgur"
__date__ ="$May 7, 2011 11:04:53 PM$"



def solve(combines, opposes, elementList):
    invokeList = []

    size = len(elementList)
    for i in range(size):
        invokeList.append(elementList[i])
        invokeSize = len(invokeList)
        if invokeSize >= 2:
            first = invokeSize - 2
            last = invokeSize - 1
            firstElem = invokeList[first]
            lastElem = invokeList[last]
            if (firstElem, lastElem) in combines.keys():
                invokeList.pop()
                invokeList.pop()
                invokeList.append(combines[(firstElem, lastElem)])
            elif (lastElem, firstElem) in combines.keys():
                invokeList.pop()
                invokeList.pop()
                invokeList.append(combines[(lastElem, firstElem)])
            else:
                for j in range(invokeSize):
                    if ((lastElem, invokeList[j]) in opposes) or ((invokeList[j], lastElem) in opposes):
                        invokeList = []
                        break

    return invokeList

def handle():
    T = 0
    solutions = []
    T = int(raw_input())
    for i in range(T):
        combineN = 0
        combineElementDict = {}
        opposeN = 0
        opposeElementList = []
        invokedElements = ""
        line = raw_input()
        elements = line.split(' ')
        combineN = int(elements[0])
        if not (combineN == 0):
            for j in range(0, len(elements[1]), 3):
                combineElementDict[(elements[1][j], elements[1][j+1])] = elements[1][j+2]
        next = 0
        if combineN == 0:
            next = 1
        else:
            next = 2
        opposeN = int(elements[next])
        if not (opposeN == 0):
            for j in range(0, len(elements[next + 1]), 3):
                opposeElementList.append((elements[next + 1][j], elements[next + 1][j+1]))

        if opposeN == 0:
            next += 2
        else:
            next += 3

        invokedElements = elements[next]

        solutions.append(solve(combineElementDict, opposeElementList, invokedElements))

    for i in range(T):
        strr = '['
        for j in range(len(solutions[i])):
            if j == len(solutions[i]) - 1:
                strr += solutions[i][j]
                break
            else:
                strr += solutions[i][j] + ', '
        strr += ']'
        print 'Case #' + str(i+1) + ': ' + strr
        
if __name__ == "__main__":
    handle()

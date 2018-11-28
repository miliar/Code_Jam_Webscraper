from collections import deque
import sys
sys.setrecursionlimit(10000)

input = open('./D-large.in', 'r').readlines()
output = open('./D-large.out', 'w') 

def kenTurn(kenStack, naomiChosen):
    kenChosen = -1
    for elem in kenStack:
        if elem > naomiChosen:
            kenChosen = elem
            kenStack.remove(elem)
            break
    if kenChosen == -1:
        kenStack.pop(0)
    return kenChosen

def war(naomiStack, kenStack, naomiScore):
    
    #naomi turn
    naomiChosen = naomiStack.pop()
    #ken turn
    kenChosen = kenTurn(kenStack, naomiChosen)
    #score
    if naomiChosen > kenChosen:
        naomiScore +=1
    if(len(naomiStack)>0):
        return war(naomiStack, kenStack, naomiScore)
    else:
        return naomiScore;


def decitefulWar(naomiStack, kenStack, naomiScore):
    #naomi turn
    if kenStack[0] > naomiStack[0]:
        naomiChosen = kenStack[-1]-0.000001
    else:
        naomiChosen = kenStack[-1]+0.000001
    naomiStack.pop(0)
    #ken turn
    kenChosen = kenTurn(kenStack, naomiChosen)
    #score
    if naomiChosen > kenChosen:
        naomiScore +=1
    if(len(kenStack)>0):
        return decitefulWar(naomiStack, kenStack, naomiScore)
    else:
        return naomiScore;
    
inputQueue = deque(input)
testCases = int(inputQueue.popleft())
for i in range(0, testCases):
    outputString = "Case #"+str(i+1)+": "
    inputQueue.popleft()
    naomiStartingStack = [float(e) for e in inputQueue.popleft().split()]
    kenStartingStack = [float(e) for e in inputQueue.popleft().split()]
    naomiStartingStack.sort()
    kenStartingStack.sort()
    warResult = war(naomiStartingStack[:], kenStartingStack[:], 0)
    decitefulWarResult = decitefulWar(naomiStartingStack, kenStartingStack, 0)
    outputString += str(decitefulWarResult) + " " + str(warResult)+"\n"
    output.write(outputString)
output.close()

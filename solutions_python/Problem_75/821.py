'''
Created on May 6, 2011

@author: iyen
'''

def intersect(a, b):
    return list(set(a) & set(b))

def main():
    filename = "B-large"
    input = open(filename+'.in')
    output = open(filename+'.out', 'w')
    
    T = int(input.readline().strip())
    
    for t in range(1,T+1):
        case = input.readline().strip("\n").split(" ")
        
        C = int(case.pop(0))
        comboDict = dict()
        for c in range(0,C):
            combo = case.pop(0)
            comboDict[(combo[0], combo[1])] = combo[2]
            
        D = int(case.pop(0))
        oppDict = dict()
        for d in range(0,D):
            oppSet = case.pop(0)
            if oppSet[0] not in oppDict:
                oppDict[oppSet[0]] = []
            oppDict[oppSet[0]].append(oppSet[1])
            if oppSet[1] not in oppDict:
                oppDict[oppSet[1]] = []
            oppDict[oppSet[1]].append(oppSet[0])
        
        N = int(case.pop(0))
        invokeList = list(case.pop(0))
        elemList = []
        lastElem = ''
        for n in range(0,N):
            elem = invokeList[n]
            # check for combo
            if (elem, lastElem) in comboDict.keys():
                elemList.pop()
                newElem = comboDict[(elem, lastElem)]
                elemList.append(newElem)
                lastElem = newElem
            elif (lastElem, elem) in comboDict.keys():
                elemList.pop()
                newElem = comboDict[(lastElem, elem)]
                elemList.append(newElem)
                lastElem = newElem
            else:
                # if no combo, check for opposing elements
                if elem in oppDict.keys():
                    oppList = oppDict[elem]
                    if len(intersect(elemList, oppList)):
                        elemList = []
                        lastElem = ''
                        continue
                # if no opposing element, append to elemList
                elemList.append(elem)
                lastElem = elem

        output.write("Case #"+str(t) + ": [")
        while len(elemList):
            output.write(elemList.pop(0))
            if len(elemList):
                output.write(", ")
            else:
                break
        output.write("]\n")
        
    
if __name__ == '__main__':
    main()
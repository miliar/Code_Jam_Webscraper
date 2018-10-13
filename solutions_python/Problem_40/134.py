import sys
import pprint

def buildTree(treeLines):

    while True:
        curLineVars = treeLines.pop(0).strip(' ()').split()
        if len(curLineVars) == 0:
            continue
        break

    if len(curLineVars) == 1:
        return {'leaf': True, 'val': float(curLineVars[0])}
    else:
        curVal = float(curLineVars[0])
        curKey = curLineVars[1]
        return {'leaf': False, 'key': curKey, 'val': curVal,
            True: buildTree(treeLines), False: buildTree(treeLines)}

if __name__ == '__main__':

    inputLines = file(sys.argv[1], 'r').read().strip().split('\n')

    #outFP = file(sys.argv[1]+'.out.txt', 'w')

    outLines = list()

    for caseNO in range(int(inputLines.pop(0).strip())):

        outLines.append('Case #%i:'%(caseNO + 1))

        dTreeLines = list()
        for dTreeLineCount in range(int(inputLines.pop(0).strip())):
            dTreeLines.append(inputLines.pop(0).strip())

        rootTree = buildTree(dTreeLines)

        animalLines = list()
        for animalCount in range(int(inputLines.pop(0).strip())):
            animalLines.append(inputLines.pop(0).strip())

        for animalLine in animalLines:
            animalVar = animalLine.split(' ')
            animalName = animalVar[0]
            animalCutes = set(animalVar[2:])
            
            cuteVal = 1
            curTreeRoot = rootTree
            while True:
                cuteVal *= curTreeRoot['val']
                if curTreeRoot['leaf']:
                    break
                curTreeRoot = curTreeRoot[curTreeRoot['key'] in animalCutes]
            outLines.append('%.7f'%cuteVal)

    #print outLines

    file(sys.argv[1]+'.out.txt', 'w').write('\n'.join(outLines))


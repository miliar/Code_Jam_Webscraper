import sys
import pprint

def procCase(caseLine):
    splitLine = caseLine.split()
    N = int(splitLine[0])

    lO = list()
    lB = list()
    seq = list()

    for v in range(0, len(splitLine)-1, 2):
        robot, button = splitLine[v+1], int(splitLine[v+2])
        if robot == 'O':
            lO.append(button)
        else:
            lB.append(button)
        seq.append(robot)


    pressed = 0
    countTime = 0

    curTurn = seq.pop(0)

    posOrange = 1
    posBlue = 1

    ptOrange = None if len(lO) == 0 else lO.pop(0)
    ptBlue = None if len(lB) == 0 else lB.pop(0)

    def itRobo(pos, pt, turn, who):
        if pt != None:
            if pos != pt:
                pos = pos+1 if pt > pos else pos-1
            elif (turn == who):
                return True, pos
        return False, pos

    while pressed != N:

        pressedO, posOrange = itRobo(posOrange, ptOrange, curTurn, 'O')
        pressedB, posBlue  = itRobo(posBlue, ptBlue, curTurn, 'B')

        if pressedO:
            ptOrange = lO.pop(0) if len(lO) != 0 else None
            pressed += 1
            curTurn = seq.pop(0) if len(seq) != 0 else None
        if pressedB:
            ptBlue = lB.pop(0) if len(lB) != 0 else None
            pressed += 1
            curTurn = seq.pop(0) if len(seq) != 0 else None

        #print pressedO, posOrange, pressedB, posBlue

        countTime += 1


    #print 'total', countTime
    return countTime




if __name__ == '__main__':

    inputLines = file(sys.argv[1], 'r').read().strip().split('\n')

    outLines = list()

    for caseNO in range(int(inputLines.pop(0).strip())):
        outLines.append('Case #%i: %s'%(caseNO + 1, procCase(inputLines.pop(0).strip())))

    #print outLines

    file(sys.argv[1]+'.out.txt', 'w').write('\n'.join(outLines))


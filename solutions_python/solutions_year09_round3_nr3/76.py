import sys
import pprint

def bribeWalk(origCells, relCells, coins):
    if len(relCells) == 0:
        #print 'end', ''.join(origCells), coins
        return coins

    curCoins = -1
    for i in range(len(relCells)):
        curCelles = origCells[:]
        curCelles[relCells[i]] = '0'
        curRelCells = relCells[:]
        curRelCells.pop(i)
        relCellIdx = relCells[i]
        curCellesStr = ''.join(curCelles)
        try:
            rCoins = curCellesStr.index('0', relCellIdx+1) - relCellIdx - 1
        except ValueError:
            rCoins = len(origCells) - relCellIdx - 1
        try:
            lCoins = relCellIdx - curCellesStr.rindex('0', 0, relCellIdx) - 1
        except ValueError:
            lCoins = relCellIdx

        #print curCellesStr, lCoins, rCoins
        rCoins = bribeWalk(curCelles, curRelCells, coins+lCoins+rCoins)
        if curCoins == -1:
            curCoins = rCoins
        else:
            if curCoins > rCoins:
                curCoins = rCoins
    return curCoins

if __name__ == '__main__':

    inputLines = file(sys.argv[1], 'r').read().strip().split('\n')

    outLines = list()

    for caseNO in range(int(inputLines.pop(0).strip())):

        outLines.append('Case #%i:'%(caseNO + 1))

        P, Q = map(int, inputLines.pop(0).strip().split(' '))

        prisonCells = ['1']*P

        releaseCells = map(lambda x: int(x)-1, inputLines.pop(0).strip().split(' '))

        rCoins = bribeWalk(prisonCells, releaseCells, 0)
        outLines[-1] = '%s %i'%(outLines[-1], rCoins if rCoins != -1 else 0)


    print outLines

    file(sys.argv[1]+'.out.txt', 'w').write('\n'.join(outLines))


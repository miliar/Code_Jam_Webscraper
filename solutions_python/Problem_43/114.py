import sys
import pprint


if __name__ == '__main__':

    inputLines = file(sys.argv[1], 'r').read().strip().split('\n')

    outLines = list()

    newBaseC = '1023456789abcdefghijklmnopqrstuvwxyz'

    for caseNO in range(int(inputLines.pop(0).strip())):

        outLines.append('Case #%i:'%(caseNO + 1))

        cryptLine = inputLines.pop(0).strip()

        pDict = dict()
        curBaseI = 0
        cCryptLine = list()
        for c in cryptLine:
            if c not in pDict:
                pDict[c] = newBaseC[curBaseI]
                curBaseI += 1
            cCryptLine.append(pDict[c])
        if curBaseI == 1:
            curBaseI += 1
        outLines[-1] = '%s %i'%(outLines[-1], int(''.join(cCryptLine), curBaseI))

    print outLines

    file(sys.argv[1]+'.out.txt', 'w').write('\n'.join(outLines))


import sys
import logging
import itertools

logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.WARNING)

def procCase(caseLine):
    iLines = caseLine

    N = int(iLines[0])
    Ci = sorted(map(int, iLines[1].split(' ')), reverse=True)

    maxValue = 0

    for iterLen in range(len(Ci)-1, 0, -1):
        for i in itertools.combinations(Ci, iterLen):
            diffCi = Ci[:]
            for c in i:
                diffCi.remove(c)
            if reduce(lambda x, y: x^y, i) != reduce(lambda x, y: x^y, diffCi):
                continue
            seanSum = sum(i)
            if seanSum > maxValue:
                maxValue = seanSum

    return 'NO' if maxValue == 0 else maxValue

    #logging.debug(N)
    #logging.debug(Ci)


def main():
    iLines = file(sys.argv[1], 'r').read().strip().split('\n')
    oLines = list()
    for caseNO in range(int(iLines.pop(0).strip())):
        logging.info('Case #%i', caseNO)
        oLines.append('Case #%i: %s'%(caseNO+1, procCase(
            [iLines.pop(0).strip(), iLines.pop(0).strip()]
            )))
        logging.info('')
    file(sys.argv[1]+'.out.txt', 'w').write('\n'.join(oLines))

if __name__ == '__main__':
    main()


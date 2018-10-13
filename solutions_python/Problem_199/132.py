inputFileName = "test.in"
# inputFileName = "A-small-attempt0.in"
inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"

global MY_DEBUG
MY_DEBUG = "test.in" == inputFileName


def calcSingleTest(f):
    line = f.readline()
    pc = list(line.split(" ")[0])
    k = int(line.split(" ")[1])
    cnt = 0
    l = len(pc)
    for i in xrange(l - k + 1):
        if pc[i] == '-':
            cnt += 1
            for j in xrange(k):
                pc[i + j] = '+' if pc[i + j] == '-' else '-'

    for j in xrange(k):
        if pc[-j] == '-':
            return 'IMPOSSIBLE'
    return str(cnt)


with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))

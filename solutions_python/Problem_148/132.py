from fractions import gcd

#inputFileName = "test.in"
#inputFileName = "A-small-attempt0.in"
#inputFileName = "A-small-attempt1.in"
#inputFileName = "A-small-attempt2.in"
#inputFileName = "A-small-attempt3.in"
inputFileName = "A-large.in"
outputFileName = inputFileName[:-3] + ".out"


def log2Exact(x):
    p = 1
    for i in xrange(0, 50):
        if x == p:
            return i
        if x < p:
            return -1
        p *= 2
    return -1


def log2(x):
    p = 1
    for i in xrange(0, 50):
        if x == p:
            return i
        if x < p:
            return i - 1
        p *= 2
    return -1


def calcSingleTest(f):
    line = f.readline()
    N = int(line.split()[0])
    X = int(line.split()[1])
    line = f.readline()
    s = map(int, line.split())
    X2 = X / 2
    s.sort()
    print s
    L = len(s)
    cnt = 0
    j = L - 1
    i = 0
    while i < j:
        s1 = s[i]
        if s1 > X2:
            break
        i += 1
        while s1 + s[j] > X and i < j:
            cnt += 1
            j -= 1
        if s1 + s[j] > X:
            break
        else:
            j -= 1
    return 1 + j + cnt

with open(inputFileName) as inpF:
    with open(outputFileName, 'w') as outF:
        line = inpF.readline()
        testsCount = int(line)
        for i in xrange(1, testsCount + 1):
            print '--------------------------------------------'
            res = calcSingleTest(inpF)
            outF.write('Case #{0}: {1}\n'.format(i, res))




